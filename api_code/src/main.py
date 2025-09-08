from fastapi import FastAPI
from api.endpoint import router

from fastapi.middleware.cors import CORSMiddleware




app = FastAPI(
    title="Investor API",
    description="API to serve investor and commitment data",
    version="1.0.0" )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
