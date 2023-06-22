from fastapi import FastAPI
from a2wsgi import ASGIMiddleware

from app.routers import user

app = FastAPI()

app.include_router(user.router, prefix="/user")

wsgi_app = ASGIMiddleware(app)

