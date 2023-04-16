from fastapi import FastAPI, HTTPException
from dotenv import dotenv_values
from src.config.database import client
from src.web_scraping.ml_scraper import MercadoLivre
from src.web_scraping.buscape_scraper import Buscape

app = FastAPI()
config = dotenv_values()

categories = ["celular", "tv", "geladeira"]


@app.on_event("startup")
def startup():
    app.mongodb_client = client
    app.database = client[config["MONGO_DB"]]


@app.get("/")
def home():
    return "API is already working"


@app.get("/products-from-buscape/{category}/{search}")
def buscape_web_scraper(category: str, search: str):
    if category not in categories:
        raise HTTPException(
            status_code=400, detail="This categorie is not available at the moment"
            )
    return Buscape.get_products(category, search)


@app.get("/products-from-ml/{category}/{search}")
def ml_web_scraper(category: str, search: str):
    if category not in categories:
        raise HTTPException(
            status_code=400, detail="This categorie is not available at the moment"
        )
    return MercadoLivre.get_products(category, search)
