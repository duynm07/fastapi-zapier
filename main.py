from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/webhook")
def webhook(payload: dict):
    # Handle the payload from Zapier
    return {"message": "Webhook received"}
