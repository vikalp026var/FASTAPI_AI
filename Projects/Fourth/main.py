from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import engine, create_tables
from routes.orders import router as orders_router
from routes.stats import router as stats_router
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(
    lifespan=lifespan
)

app.include_router(orders_router)
app.include_router(stats_router)

@app.get('/')
async def root():
    return {'message': 'Hello World'}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)