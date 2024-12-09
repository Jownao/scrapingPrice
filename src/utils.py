import time
from .fetcher import fetch_page, parse_page

def validate_selectors(url, product_selector, price_selector):
    """Valida os seletores fornecidos pelo usuário."""
    print("Testando os seletores...")
    try:
        page_content = fetch_page(url)
        data = parse_page(page_content, product_selector, price_selector)
        print(f"Seletores validados! Produto: {data['product_name']}, Preços: {data['prices']}")
    except ValueError as e:
        raise ValueError(f"Erro nos seletores: {e}")
