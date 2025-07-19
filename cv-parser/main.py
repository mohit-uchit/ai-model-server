from fastapi import FastAPI, UploadFile, File
import PyPDF2

app = FastAPI()

@app.post("/extract/")
async def extract(pdf: UploadFile = File(...)):
    text = ""
    try:
        reader = PyPDF2.PdfReader(pdf.file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    except Exception as e:
        return {"error": str(e)}
    return {"text": text}