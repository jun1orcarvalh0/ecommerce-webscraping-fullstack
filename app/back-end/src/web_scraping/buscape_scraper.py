import requests
from fastapi import HTTPException
from dotenv import dotenv_values
from src.config.database import client
from bs4 import BeautifulSoup

config = dotenv_values()
database = client[config["MONGO_DB"]]

buscape_collection = database.buscape


class Buscape():
    def get_products(category, search):
        check_db_data = buscape_collection.find_one(
            {"category": category, "search": search}, {"_id": 0})
        if check_db_data:
            return check_db_data
        if check_db_data is None:
            return get_products_from_buscape(category, search)


def get_products_from_buscape(category, search):
    BASE_URL = 'https://www.buscape.com.br'
    URL = f"{BASE_URL}/{category}/{search}"
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []

    for product in soup.find_all(
            'div', class_='SearchCard_ProductCard__1D3ve')[:3]:
        new_product = {}
        new_product["picture"] = product.find('img')['src']
        new_product["title"] = product.find(
            'h2', class_='SearchCard_ProductCard_Name__ZaO5o'
            ).text.strip()
        new_product["price"] = product.find(
            'p', class_='Text_Text__h_AF6 Text_MobileHeadingS__Zxam2'
            ).text.replace(',', '.').replace('R$', '').replace(' ', '')
        new_product["link"] = BASE_URL + product.find('a')['href']
        new_product["category"] = category
        products.append(new_product)

    if len(products) == 0:
        raise HTTPException(
            status_code=404,
            detail="Not Found Error"
        )

    save_data = save_scraping_on_db(category, search, products)
    return save_data


def save_scraping_on_db(category, search, products):
    buscape_collection.insert_one(
        {"category": category, "search": search, "products": products}
        )
    check_db_data = buscape_collection.find_one(
            {"category": category, "search": search}, {"_id": 0})
    return check_db_data
