from fastapi import FastAPI, UploadFile, File
import shutil
from fastapi.responses import JSONResponse
from mainrunner import run_sys
from fastapi.middleware.cors import CORSMiddleware
import pytesseract

import os

pytesseract.pytesseract.tesseract_cmd = "/opt/anaconda3/bin/tesseract"
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods= ["*"],
    allow_headers=["*"],
)

upload_folder = "uploads"
os.makedirs(upload_folder, exist_ok=True)
model_path = "/Users/siaaggarwal/Downloads/bert:model"
# @app.get()

@app.post("/analyze")
async def analyze_contract(file:UploadFile=File(...)):
    filepath = os.path.join(upload_folder, file.filename)
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # file=f"emp_{file.filename}"
    # with open(file, "wb") as write:
    #     #
    #     code
    # model_path = ""
    # return [
    #     {
    #         "text": f"Received file: {file.filename}",
    #         "type": "Liability",
    #         "confidence": 0.92,
    #         "risk_score": 8,
    #         "risk_reason": f"File size read successfully"
    #     }
    # ]
    result = run_sys(filepath, model_path)
    return result
    # return JSONResponse(content=result)
