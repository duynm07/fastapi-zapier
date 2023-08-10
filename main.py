from io import BytesIO
from typing import Optional

from fastapi import APIRouter, File, UploadFile, FastAPI
from fastapi.responses import JSONResponse
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