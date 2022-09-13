from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from mangum import Mangum
from .routers import user

if settings.environment == 'PROD':
    app = FastAPI(openapi_url=None, redoc_url=None)
else:
    app = FastAPI()

origins = [settings.origin_0]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/health')
def check_health():
    return {"health": "healthy"}
  
app.include_router(user.router)

handler = Mangum(app)