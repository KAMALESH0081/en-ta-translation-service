import os
import torch
from model import model
from tokenizer import WordLevelTokenizer

tamil_tokenizer = WordLevelTokenizer.load("assets/tamil_tokenizer.json")
english_tokenizer = WordLevelTokenizer.load("assets/english_tokenizer.json")

# ---------------- GLOBAL SETUP ----------------
device = torch.device('cpu')

model.to(device)
model.eval()

checkpoint_path = "assets/Model_Params.pth"
   
if os.path.exists(checkpoint_path):
    model.load_state_dict(torch.load(checkpoint_path, map_location=torch.device(device)))
    print("Model loaded")
else :
    print("Model not loaded")


# ---------------- MAIN FUNCTION ----------------
def translate(text, max_len=24):

    def causal_mask(size):
        mask = torch.triu(torch.ones((1, size, size), device=device), diagonal=1).int()
        return mask == 0

    def pad_sequence(tokens):
        tokens = [2] + tokens + [3]  # CLS, SEP

        if len(tokens) < max_len:
            tokens += [1] * (max_len - len(tokens))
        else:
            tokens = tokens[:max_len]

        return tokens

    def greedy_decode(source, source_mask):
        sos_idx, eos_idx = 2, 3

        encoder_output = model.encoder(source, source_mask)

        decoder_input = torch.full((1, 1), sos_idx, dtype=torch.long, device=device)

        while decoder_input.size(1) < max_len:
            decoder_mask = causal_mask(decoder_input.size(1))

            out = model.decoder(
                decoder_input,
                encoder_output,
                source_mask,
                decoder_mask
            )

            next_word = torch.argmax(out[:, -1], dim=1)

            if next_word.item() == eos_idx:
                break

            decoder_input = torch.cat(
                [decoder_input, next_word.unsqueeze(1)],
                dim=1
            )

        return decoder_input.squeeze(0)[1:]

    # ---------------- PIPELINE ----------------
    with torch.no_grad():
        tokens = english_tokenizer.encode(text)
        tokens = pad_sequence(tokens)

        sentence = torch.tensor(tokens, dtype=torch.long).to(device)

        encoder_input = sentence.unsqueeze(0)
        encoder_mask = (sentence != 1).unsqueeze(0).unsqueeze(0).int().to(device)

        output_tokens = greedy_decode(encoder_input, encoder_mask)

        output_text = tamil_tokenizer.decode(output_tokens.cpu().tolist())

    return output_text