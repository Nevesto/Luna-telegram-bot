# make scraper for bitcoin price using playwright

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def bit():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        page = browser.new_page()
        page.goto("https://www.google.com/search?q=pre%C3%A7o+do+bitcoin&oq=pre%C3%A7o+&aqs=chrome.1.69i57j35i39l2j0i131i433i512l2j0i457i512j0i402l2j0i67l2.2303j1j7&sourceid=chrome&ie=UTF-8")
        page.is_visible('.card-section > div:nth-child(2)')
        html = page.inner_html('.card-section')
        soup = BeautifulSoup(html, 'html.parser')
        price = soup.find('span', {'class': 'pclqee'}).text
        print(f'O preço do bitcoin atual é: {price} BRL')