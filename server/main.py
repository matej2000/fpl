from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from helper import getManagerData, getHistory, getTeamData, getGeneralInfo

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/manager")
async def manager(id:int):
    try:
        id2 = int(id)
        if id2>0 and id2<10000000:
            return  getManagerData(id2)
    except ValueError:
        return HTTPException(status_code=422, detail="Unprocessable Entity")
    return HTTPException(status_code=422, detail="Unprocessable Entity")

@app.get("/history")
async def history(id:int):
    try:
        id2 = int(id)
        if id2>0 and id2<10000000:
            return  getHistory(id2)
    except ValueError:
        return HTTPException(status_code=422, detail="Unprocessable Entity")
    return HTTPException(status_code=422, detail="Unprocessable Entity")

@app.get("/team")
async def team(id:int, event:int):
    try:
        id2 = int(id)
        if id2>0 and id2<10000000:
            return  getTeamData(id2, event)
    except ValueError:
        return HTTPException(status_code=422, detail="Unprocessable Entity")
    return HTTPException(status_code=422, detail="Unprocessable Entity")

@app.get("/info")
async def info():
    try:
        return  getGeneralInfo()
    except ValueError:
        return HTTPException(status_code=422, detail="Unprocessable Entity") #FIXME: change error code

