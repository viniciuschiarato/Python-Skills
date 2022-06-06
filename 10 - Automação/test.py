from playwright.sync_api import sync_playwright
from time import sleep

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto('https://translate.google.com.br/?hl=pt-BR&sl=en&tl=pt&op=translate')
    pagina.locator('xpath=//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/'
                   'c-wiz[1]/span/span/div/textarea').click()  # hover() (mouse sobre o xpath)
    sleep(45)
