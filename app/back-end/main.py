from fastapi import FastAPI
from src.web_scraping.buscape_scraper import Buscape
from src.web_scraping.ml_scraper import MercadoLivre

app = FastAPI()


@app.get("/")
def home():
    return "API is already working"


@app.get("/products-from-buscape/{category}/{search}")
def buscape_web_scraper(category: str, search: str):
    return Buscape.get_products(category, search)


@app.get("/products-from-ml/{category}/{search}")
def ml_web_scraper(category: str, search: str):
    return MercadoLivre.get_products(category, search)
