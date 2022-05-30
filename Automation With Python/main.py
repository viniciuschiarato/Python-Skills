from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto('https://translate.google.com.br/?hl=pt-BR&sl=en&tl=pt&op=translate')
