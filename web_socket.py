import datetime as dt
import random
import time

from fastapi import APIRouter, WebSocket


socket = APIRouter(
    prefix="/ws",
    tags=["WebSocket"]
)


@socket.get("/")
async def index():
    return True


@socket.websocket("/random")
async def random_number(ws: WebSocket):
    await ws.accept()
    while True:
        # data = await ws.receive_text()
        # print(data, type(data))
        # print(ws.base_url, ws.cookies)
        response = random.randint(1, 100)
        await ws.send_text(f"Random Response: {response} At [{dt.datetime.now()}]")
        time.sleep(3)
