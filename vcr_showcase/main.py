from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse

from vcr_showcase.api.endpoints.users import router as users_router

app = FastAPI()
app.include_router(users_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/status")
def status() -> JSONResponse:
    return JSONResponse(content={"status": "ok"})


@app.get("/")
def docs() -> RedirectResponse:
    return RedirectResponse("/docs")


@app.exception_handler(HTTPException)
def http_exception_handler(_, exception: HTTPException) -> JSONResponse:
    return JSONResponse(
        status_code=exception.status_code, content={"message": exception.detail}
    )


@app.exception_handler(Exception)
def internal_error_exception_handler(*_: Any) -> JSONResponse:
    return JSONResponse(status_code=500, content={"message": "Internal server error"})
