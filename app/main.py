from fastapi import FastAPI
from app.routes.v1.api import api_router



app = FastAPI(
    title="Hostel Billing System",
    version="1.0.0"
)

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Hostel Billing System"}
