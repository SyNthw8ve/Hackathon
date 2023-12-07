import asyncpg
from asyncio.exceptions import TimeoutError

from fastapi import FastAPI, status, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from hera.server.api.heath_professional.route import router as health_professional_router

from hera.server.database import Base, engine

app = FastAPI()

@app.on_event("startup")
async def startup_event():

    try:

        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    except (ConnectionRefusedError, TimeoutError):

        print("Database connection timeout")

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"detail": [error["msg"] for error in exc.errors()]}),
    )

app.include_router(health_professional_router)

@app.get("/")
async def root():
    return { "message": "Server Up!" }

