from fastapi import FastAPI

from web_socket import socket

app = FastAPI(
    title="WebSocket Application",
    redoc_url=None
)


@app.get("/", tags=["Test"])
async def index():
    """
        Index Route
    """
    return "WebSocket Application!"

app.include_router(socket)
