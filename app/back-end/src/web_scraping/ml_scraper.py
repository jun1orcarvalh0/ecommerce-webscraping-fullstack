import requests
from bs4 import BeautifulSoup


class MercadoLivre:
    def get_products(category, search):
        if (category == 'celular'):
            produtos = get_mobile_products(category, search)
            return produtos

        elif (category == 'tv'):
            produtos = get_tv_products(category, search)
            return produtos

        else:
            produtos = get_refrigerator_products(category, search)
            return produtos


def get_mobile_products(category, search):
    URL = f'https://lista.mercadolivre.com.br/celulares-telefones/{search}'
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []

    for product in soup.find_all(
            'li', class_='ui-search-layout__item')[:3]:
        new_product = {}
        new_product["picture"] = product.find()["data-src"]
        new_product["title"] = product.find(
            'h2', class_='ui-search-item__title shops__item-title'
            ).text.strip()
        new_product["price"] = product.find(
            'span', class_='price-tag-fraction'
            ).text
        new_product["link"] = product.find('a')['href']
        new_product["category"] = category
        products.append(new_product)
    return products


def get_tv_products(category, search):
    URL = f'https://lista.mercadolivre.com.br/tv-{search}'
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []

    for product in soup.find_all(
            'li', class_='ui-search-layout__item')[:3]:
        new_product = {}
        new_product["picture"] = product.find()["data-src"]
        new_product["title"] = product.find(
            'h2', class_='ui-search-item__title shops__item-title'
            ).text.strip()
        new_product["price"] = product.find(
            'span', class_='price-tag-fraction'
            ).text
        new_product["link"] = product.find('a')['href']
        new_product["category"] = category
        products.append(new_product)
    return products


def get_refrigerator_products(category, search):
    URL = f'https://lista.mercadolivre.com.br/geladeira-{search}'
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []

    for product in soup.find_all(
            'li', class_='ui-search-layout__item')[:3]:
        new_product = {}
        new_product["picture"] = product.find()["data-src"]
        new_product["title"] = product.find(
            'h2', class_='ui-search-item__title shops__item-title'
            ).text.strip()
        new_product["price"] = product.find(
            'span', class_='price-tag-fraction'
            ).text
        new_product["link"] = product.find('a')['href']
        new_product["category"] = category
        products.append(new_product)
    return products
