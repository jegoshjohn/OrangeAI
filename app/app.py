from fastapi import FastAPI
from fastapi.responses import RedirectResponse, JSONResponse
from starlette.middleware.cors import CORSMiddleware
from api.v1.api import api_router
from mangum import Mangum
import uvicorn
from utils.common import logger

logger.info("Starting the app")

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

handler = Mangum(app)


@app.get("/health_check")
async def health_check():
    logger.info("Health check")
    return JSONResponse({"health_status": "ok"})

@app.get("/")
async def root_redirect():
    return RedirectResponse(url="/docs")

app.include_router(api_router, prefix="/api/v1")


if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8080)
