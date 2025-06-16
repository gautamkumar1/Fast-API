from fastapi import FastAPI
from utils.db import connect_db,disconnect_db


async def lifespan(app: FastAPI):
    await connect_db()
    yield
    await disconnect_db()
app = FastAPI(lifespan=lifespan)

