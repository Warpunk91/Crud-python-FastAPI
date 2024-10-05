from fastapi import FastAPI 
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from .controllers import controller
from starlette.requests import Request

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="myApp/static"), name="static")

templates = Jinja2Templates(directory="myApp/templates")

app.include_router(controller.appRouter)

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})