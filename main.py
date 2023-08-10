from io import BytesIO
from typing import Optional

from fastapi import APIRouter, File, UploadFile, FastAPI
from fastapi.responses import JSONResponse
from PIL import Image
from starlette import status

app = FastAPI()

@app.post("/test", status_code=status.HTTP_200_OK)
async def ocr(file: UploadFile = File(...)):
    try:
        file_data = file.read()
        print(file_data)
        # image_data = await file.read()
        # image = Image.open(BytesIO(image_data)).convert("RGB")

        return JSONResponse(content={"message": "Success"})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
