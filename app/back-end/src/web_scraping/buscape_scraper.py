import requests
from bs4 import BeautifulSoup


class Buscape():
    def get_products(category, search):
        BASE_URL = 'https://www.buscape.com.br'
        URL = f"{BASE_URL}/{category}/{search}"
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')

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
                ).text.replace(',', '.')
            new_product["link"] = BASE_URL + product.find('a')['href']
            new_product["category"] = category
            products.append(new_product)
        return products
