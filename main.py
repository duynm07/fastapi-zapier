from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("https://hooks.zapier.com/hooks/catch/16132664/31x07ar/")
def webhook(payload: dict):
    # Handle the payload from Zapier
    print("Received data:", payload)
    return {"message": "Webhook received"}
