from fastapi import FastAPI, Form
from transformers import pipeline

app = FastAPI()
qg_pipeline = pipeline("text2text-generation", model="valhalla/t5-base-qg-hl")

@app.post("/generate/")
async def generate(context: str = Form(...)):
    question = qg_pipeline(context)[0]['generated_text']
    return {"question": question}