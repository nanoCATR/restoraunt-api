from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn
from starlette.middleware.base import BaseHTTPMiddleware

from middleware import log_middleware
from api.tables import router as table_router
from api.reservations import router as reservations_router


load_dotenv()
app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)


app.include_router(table_router.router, prefix="/table", tags=["Table"])
app.include_router(reservations_router.router, prefix="/reservation", tags=["Reservation"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=80, reload=True)