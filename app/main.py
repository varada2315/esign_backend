from fastapi import FastAPI
from app.routes import sign

app = FastAPI(title="eSign Backend with Face Verification")

app.include_router(sign.router)

@app.get("/")
def root():
    return {"message": "API is running"}