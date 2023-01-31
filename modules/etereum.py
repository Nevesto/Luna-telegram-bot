# make scraper for etereum price using playwright

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def eth():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        page = browser.new_page()
        page.goto("https://www.google.com/search?q=pre%C3%A7o+do+ethereum&sxsrf=AJOqlzX77xFmaY5JDkeLBVKuolYmh3u4Mg%3A1675160680418&ei=aOzYY7eZGZSH1sQPybqEyAo&ved=0ahUKEwi37bDqy_H8AhWUg5UCHUkdAakQ4dUDCA8&uact=5&oq=pre%C3%A7o+do+ethereum&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCkoECEEYAEoECEYYAFAAWABgvgloAHABeACAAX-IAX-SAQMwLjGYAQCgAQKgAQHAAQE&sclient=gws-wiz-serp")
        page.is_visible('.card-section > div:nth-child(2)')
        html = page.inner_html('.card-section')
        soup = BeautifulSoup(html, 'html.parser')
        price = soup.find('span', {'class': 'pclqee'}).text
        print(f'O preço do etereum atual é: {price} BRL')
        browser.close()
eth()