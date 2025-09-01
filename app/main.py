from fastapi import FastAPI
from app.routers import patients, medicines

app = FastAPI()

app.include_router(patients.router)
app.include_router(medicines.router)
