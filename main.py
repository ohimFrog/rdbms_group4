from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from database import init_db
from handlers import (
    lang_router,
    company_router,
    drug_router,
    user_router,
    feedback_router
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event handler - runs on startup and shutdown"""
    # Startup: Create all tables
    try:
        print("Initializing database...")
        init_db()
        print("Database initialization complete!")
    except Exception as e:
        print(f"Failed to initialize database: {e}")
        print("Server will start but database operations may fail.")

    yield

    # Shutdown: cleanup if needed
    print("Shutting down...")


app = FastAPI(title="Drug Database API", version="1.0.0", lifespan=lifespan)

routers = [
    lang_router,
    company_router,
    drug_router,
    user_router,
    feedback_router
]

for router in routers:
    app.include_router(router)


@app.get("/")
def root():
    return {"message": "Drug Database API", "docs": "/docs"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
