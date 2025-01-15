from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, Base
from app.api import users

from contextlib import asynccontextmanager
import logging
import sys

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stdout
)

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan management with proper error handling and logging"""
    # 启动时创建数据库表
    try:
        logger.info("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Failed to create database tables: {str(e)}")
        raise
    
    try:
        yield
    finally:
        logger.info("Application shutdown initiated")
        # Add any cleanup logic here if needed

app = FastAPI(
    lifespan=lifespan,
    title="FastAPI Application",
    description="FastAPI application with SQLAlchemy integration",
    version="1.0.0"
)

# CORS (Cross-Origin Resource Sharing) configuration
# Allows requests from any origin (*) with all HTTP methods and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,  # Allow credentials (cookies, authorization headers)
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include API routers
# This mounts the users router at /users endpoint
app.include_router(
    users.router,  # Router containing user-related endpoints
    prefix="/users"  # All routes will be prefixed with /users
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application"}
