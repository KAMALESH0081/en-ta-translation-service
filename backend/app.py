# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from inference import translate

app = FastAPI()

class Request(BaseModel):
    text: str

@app.post("/translate")
def translate_api(req: Request):
    result = translate(req.text)
    print(f"Translated: {result}")
    return {"translation": result}