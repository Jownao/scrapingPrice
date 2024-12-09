import requests
from bs4 import BeautifulSoup
import time

def fetch_page(url):
    """Faz a requisição HTTP e retorna o conteúdo da página."""
    response = requests.get(url)
    return response.text

def parse_page(html, product_selector, price_selector):
    """Extrai dados da página com base nos seletores CSS."""
    soup = BeautifulSoup(html, 'html.parser')
    try:
        product_name = soup.select_one(product_selector).get_text(strip=True)
        prices = [int(price.get_text(strip=True).replace('.', '').replace(',', '')) 
                  for price in soup.select(price_selector)]
    except Exception as e:
        raise ValueError(f"Erro ao processar os seletores: {e}")

    return {
        'product_name': product_name,
        'prices': prices,
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
    }
