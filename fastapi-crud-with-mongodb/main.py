from fastapi import FastAPI
from routes.user_routes import router as user_router
# from routes.auth_routes import router as authrouter
from routes.auth_routes import router as auth_router

app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)