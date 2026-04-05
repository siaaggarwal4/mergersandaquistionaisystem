from fastapi import FastAPI, UploadFile, File
import shutil
from fastapi.responses import JSONResponse
from mainrunner import run_sys
import os

app=FastAPI()

upload_folder = "uploads"
os.makedirs(upload_folder, exist_ok=True)


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

    result = run_sys(filepath, "model_path")

    return JSONResponse(content=result)
