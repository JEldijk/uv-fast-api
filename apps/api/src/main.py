from fastapi import FastAPI
from utils.logging import Format, LogLevels, init_logging

from .config import CommonSettings

LOG = init_logging(format=Format.console, log_level=LogLevels.DEBUG)

app = FastAPI()


@app.get("/info")
async def info(settings: CommonSettings):
    if not settings.admin_email:
        raise ValueError("admin_email is required")

    LOG.error(f"admin_email: {settings.admin_email}")
    return settings.model_dump_json()
