from fastapi import FastAPI

from controllers.client_router import client_router

app = FastAPI(
    root_path="/api",
    title="FastAPI with SQLAlchemy",
    version="0.0.1",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(client_router, prefix="/clients", tags=["Clients"])
