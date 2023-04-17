from decouple import config
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.config.database import client
from src.web_scraping.ml_scraper import MercadoLivre
from src.web_scraping.buscape_scraper import Buscape

app = FastAPI()
MONGO_DB_DATABASE = config("MONGO_DB")

categories = ["celular", "tv", "geladeira"]


@app.on_event("startup")
def startup():
    app.mongodb_client = client
    app.database = client[MONGO_DB_DATABASE]


app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return "API is already working"


@app.get("/products-from-buscape/{category}/{search}")
def buscape_web_scraper(category: str, search: str):
    if category not in categories:
        raise HTTPException(
            status_code=400,
            detail="This categorie is not available at the moment"
            )
    return Buscape.get_products(category, search)


@app.get("/products-from-ml/{category}/{search}")
def ml_web_scraper(category: str, search: str):
    if category not in categories:
        raise HTTPException(
            status_code=400,
            detail="This categorie is not available at the moment"
        )
    return MercadoLivre.get_products(category, search)
