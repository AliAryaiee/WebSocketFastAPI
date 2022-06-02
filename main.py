from fastapi import FastAPI

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
