import asyncio
from src.database import create_connection, setup_database, save_to_database
from src.fetcher import fetch_page, parse_page
from src.telegram_bot import send_message
from src.utils import validate_selectors

async def main():
    conn = create_connection()
    setup_database(conn)

    # Solicita os detalhes da página ao usuário
    url = input("Insira a URL da página do produto: ")
    product_selector = input("Insira o seletor CSS para o nome do produto: ")
    price_selector = input("Insira o seletor CSS para os preços (vários preços, se houver): ")

    # Valida os seletores fornecidos
    try:
        validate_selectors(url, product_selector, price_selector)
    except ValueError as e:
        print(e)
        return

    try:
        while True:
            # Faz a requisição e parseia a página
            page_content = fetch_page(url)
            product_info = parse_page(page_content, product_selector, price_selector)

            # Salva os dados no banco de dados SQLite
            save_to_database(conn, product_info)
            print("Dados salvos no banco:", product_info)

            # Envia mensagem ao Telegram com os preços
            message = f"Produto: {product_info['product_name']}\nPreços: {product_info['prices']}"
            await send_message(message)

            # Aguarda 10 segundos antes da próxima execução
            await asyncio.sleep(10)

    except KeyboardInterrupt:
        print("Parando a execução...")
    finally:
        conn.close()

if __name__ == "__main__":
    asyncio.run(main())
