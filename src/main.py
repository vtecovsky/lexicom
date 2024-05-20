from fastapi import FastAPI

from src.api import router
from src.dependencies import Dependencies
from src.repositories.client import ClientRepository
from src.storage.redis import RedisStorage


async def lifespan(app: FastAPI):
    storage = RedisStorage()
    await storage.initialize()
    client_repository = ClientRepository(storage)
    Dependencies.set_client_repository(client_repository)
    yield
    await storage.close()


app = FastAPI(lifespan=lifespan)
app.include_router(router)
