from fastapi import FastAPI 
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from .controllers import controller
from starlette.requests import Request

# Crear las tablas
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Para permitir todas las peticiones de orígenes distintos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar los archivos estáticos
app.mount("/static", StaticFiles(directory="myApp/static"), name="static")

# Configurar las plantillas HTML
templates = Jinja2Templates(directory="myApp/templates")

# Incluir las rutas del controlador
app.include_router(controller.appRouter)

# Ruta para mostrar la página principal con HTML
@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})