from fastapi import FastAPI
from .config import CommonSettings

app = FastAPI()


@app.get("/info")
async def info(settings: CommonSettings):
    if not settings.admin_email:
        raise ValueError("admin_email is required")
    return settings.model_dump_json()
