# This file contains the implementation for the Coqui TTS API.

from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
import coqui_tts
import uuid
import os

app = FastAPI()
tts = coqui_tts.TTS()

@app.post("/synthesize/")
async def synthesize(text: str = Form(...)):
    output_file = f"output_{uuid.uuid4().hex}.wav"
    tts.synthesize(text, output_file)
    response = FileResponse(output_file, media_type="audio/wav")
    # Optionally, cleanup after sending
    # os.remove(output_file)
    return response