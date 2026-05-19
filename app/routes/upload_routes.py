from fastapi import APIRouter, UploadFile, File
import shutil
import os


router = APIRouter()


os.makedirs("../storage", exist_ok=True)


@router.post("/upload")
def upload_pdf(file: UploadFile = File(...)):

    file_path = f"../storage/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "mensagem": "PDF enviado com sucesso",
        "arquivo": file.filename
    }