import requests
from dotenv import dotenv_values
from src.config.database import client
from bs4 import BeautifulSoup

config = dotenv_values()
database = client[config["MONGO_DB"]]

mercadolivre_collection = database.mercadolivre

BASE_URL = 'https://lista.mercadolivre.com.br'


class MercadoLivre:
    def get_products(category, search):
        check_db_data = mercadolivre_collection.find_one(
            {"category": category, "search": search}, {"_id": 0})
        if check_db_data:
            return check_db_data
        if check_db_data is None:
            return get_products_from_ml(category, search)


def get_products_from_ml(category, search):
    if (category == 'celular'):
        return get_mobile_products(category, search)

    elif (category == 'tv'):
        return get_tv_products(category, search)

    else:
        return get_refrigerator_products(category, search)


def get_mobile_products(category, search):
    URL = f'{BASE_URL}/celulares-telefones/celulares-smartphones/{search}'
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []

    for product in soup.find_all(
            'li', class_='ui-search-layout__item')[:3]:
        new_product = {}
        new_product["picture"] = product.find('img')["data-src"]
        new_product["title"] = product.find(
            'h2', class_='ui-search-item__title shops__item-title'
            ).text.strip()
        new_product["price"] = product.find(
            'span', class_='price-tag-fraction'
            ).text
        new_product["link"] = product.find('a')['href']
        new_product["category"] = category
        products.append(new_product)

    save_data = save_scraping_on_db(category, search, products)
    return save_data


def get_tv_products(category, search):
    URL = f'{BASE_URL}/tv-{search}'
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []

    for product in soup.find_all(
            'li', class_='ui-search-layout__item')[:3]:
        new_product = {}
        new_product["picture"] = product.find('img')["data-src"]
        new_product["title"] = product.find(
            'h2', class_='ui-search-item__title shops__item-title'
            ).text.strip()
        new_product["price"] = product.find(
            'span', class_='price-tag-fraction'
            ).text
        new_product["link"] = product.find('a')['href']
        new_product["category"] = category
        products.append(new_product)

    save_data = save_scraping_on_db(category, search, products)
    return save_data


def get_refrigerator_products(category, search):
    URL = f'{BASE_URL}/geladeira-{search}'
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []

    for product in soup.find_all(
            'li', class_='ui-search-layout__item')[:3]:
        new_product = {}
        new_product["picture"] = product.find('img')["data-src"]
        new_product["title"] = product.find(
            'h2', class_='ui-search-item__title shops__item-title'
            ).text.strip()
        new_product["price"] = product.find(
            'span', class_='price-tag-fraction'
            ).text
        new_product["link"] = product.find('a')['href']
        new_product["category"] = category
        products.append(new_product)

    save_data = save_scraping_on_db(category, search, products)
    return save_data


def save_scraping_on_db(category, search, products):
    mercadolivre_collection.insert_one(
        {"category": category, "search": search, "products": products}
        )
    check_db_data = mercadolivre_collection.find_one(
            {"category": category, "search": search}, {"_id": 0})
    return check_db_data
