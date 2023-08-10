import datetime
import io
import os
import zipfile
from io import BytesIO
from typing import Optional

from fastapi import APIRouter, FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from pdf2image import convert_from_bytes, convert_from_path
from starlette import status

app = FastAPI()

@app.post("/test", status_code=status.HTTP_200_OK)
async def ocr(file: UploadFile = File(...)):
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    print("New request", formatted_datetime)
    try:
        file_data = file.read()
        # image_data = await file.read()
        # image = Image.open(BytesIO(image_data)).convert("RGB")

        return JSONResponse(content={"message": "Success"})
    except Exception as e:
        print(f">>> Error: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.post("/tests", status_code=status.HTTP_200_OK)
async def ocr(my_str: str):
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    print("New request", formatted_datetime, my_str)
    try:
        
        return JSONResponse(content={"message": "Success", "content": my_str})
    except Exception as e:
        print(f">>> Error: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@app.post("/convert_pdf_to_images/")
async def convert_pdf_to_images(pdf_file: UploadFile = File(...)):
    # Create a temporary directory to store images
    print(">>> convert_pdf_to_images")
    temp_dir = "temp_images"
    os.makedirs(temp_dir, exist_ok=True)

    # Save the uploaded PDF file
    pdf_path = os.path.join(temp_dir, pdf_file.filename)
    with open(pdf_path, "wb") as pdf_buffer:
        pdf_buffer.write(pdf_file.file.read())

    # Convert PDF pages to images
    images = convert_from_path(pdf_path)
    print(f">>> Converted {len(images)} pages to images.")

    # Save images and collect their paths
    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(temp_dir, f"page_{i+1}.jpg")
        image.save(image_path, "JPEG")
        image_paths.append(image_path)

    # Create a zip file containing images
    zip_path = os.path.join(temp_dir, "images.zip")
    print(f">>> Zipping ...")
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for image_path in image_paths:
            zipf.write(image_path, os.path.basename(image_path))

    # Clean up temporary images
    for image_path in image_paths:
        os.remove(image_path)
    os.remove(pdf_path)

    print(f">>> Ready to download.")
    # Return the zip file
    return FileResponse(zip_path, headers={"Content-Disposition": "attachment; filename=images.zip"})