from fastapi import FastAPI
from sqlalchemy import text
from app.db import engine

app = FastAPI(title="Proyecto Alojamiento - API")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Backend del proyecto de alojamientos funcionando 🚀"}

@app.get("/db-check")
def db_check():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1")).scalar()
    return {"db": "ok", "result": result}
