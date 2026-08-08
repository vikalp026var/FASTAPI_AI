from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables, get_session

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    print("Tables created successfully.")
    yield
    #shutdown: clean
    print("Application shutdown. Cleanup done.")
    

app = FastAPI(
    title="Rangmanch API",
    description="API for managing rangmanch data",
    lifespan=lifespan
)

@app.get("/")
def root():
    return {
        "message": "Welcome to the rangemanch API"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

