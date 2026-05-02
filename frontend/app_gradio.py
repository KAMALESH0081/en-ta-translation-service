# gradio_app.py
import gradio as gr
import requests

def call_api(text):
    response = requests.post(
        "http://backend:8000/translate",
        json={"text": text}
    )
    return response.json()["translation"]

gr.Interface(
    fn=call_api,
    inputs="text",
    outputs="text"
).launch(server_name="0.0.0.0", server_port=7860)