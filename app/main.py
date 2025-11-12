from fastapi import FastAPI
from app.routers import characters
from app.seed import init_db

app = FastAPI(title="Game Character API", version="1.0")
app.include_router(characters.router)

@app.on_event("startup")
def startup_event():
    init_db()
