from fastapi import FastAPI,APIRouter
from utils.db import connect_db,disconnect_db
from router.userRoute import router as user_router

async def lifespan(app: FastAPI):
    await connect_db()
    yield
    await disconnect_db()
app = FastAPI(lifespan=lifespan)
app.include_router(user_router, prefix="/user", tags=["user"])


