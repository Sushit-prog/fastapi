from fastapi import FastAPI
from src.utils.db import Base, engine
l


Base.metadata.create_all(engine)

app = FastAPI(title="Task Management API")