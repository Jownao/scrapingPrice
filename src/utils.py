import time
from fetcher import fetch_page, parse_page

def validate_selectors(url, product_selector, price_selector):
    """Valida os seletores fornecidos pelo usuário."""
    print("Testando os seletores...")
    try:
        page_content = fetch_page(url)
        data = parse_page(page_content, product_selector, price_selector)
        print(f"Seletores validados! Produto: {data['product_name']}, Preços: {data['prices']}")
    except ValueError as e:
        raise ValueError(f"Erro nos seletores: {e}")

url = "https://www.amazon.com.br/Samsung-Processador-Qualcomm-Snapdragon-Qu%C3%A1drupla/dp/B0BRT5Y13B/ref=pd_ci_mcx_mh_mcx_views_0_title"
product_selector = "#productTitle"
price_selector = "#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay.selectorgadget_rejected > span:nth-child(2) > span.a-price-whole"
validate_selectors(url, product_selector, price_selector)

#productTitle
#corePrice_feature_div > div > div > span.a-price.aok-align-center > span:nth-child(2) > span.a-price-whole