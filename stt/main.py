from fastapi import FastAPI, UploadFile, File
import whisper, os

app = FastAPI()
model = whisper.load_model("base")

@app.post("/transcribe/")
async def transcribe(audio: UploadFile = File(...)):
    with open("temp.wav", "wb") as f:
        f.write(await audio.read())
    result = model.transcribe("temp.wav")
    os.remove("temp.wav")
    return {"text": result["text"]}