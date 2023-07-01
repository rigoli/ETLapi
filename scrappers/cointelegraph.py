import sys
import time
from urllib.parse import urlparse, parse_qs

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class ScraperCointelegraph:
    def __init__(self, keyword, headless=False):
        options = webdriver.ChromeOptions()
        if headless: options.add_argument('headless')
        self.driver = webdriver.Chrome(executable_path="./scrappers/chromedriver", options=options)
        self.url_base = "https://cointelegraph.com/tags/"+keyword

    def get_news(self, num_news):
        news = []
        num_news = int(num_news)

        try:
            self.driver.get(self.url_base)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'tag-page__title')))

            while len(news) < num_news:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                try:
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'posts-listing__item')))
                except TimeoutException:
                    print("Tiempo de espera excedido después de 10 segundos.")
                    break

                news_elements = self.driver.find_elements(By.CLASS_NAME, "posts-listing__item")

                for element in news_elements:
                    if len(news) >= num_news:
                        break

                    title = element.find_element(By.CLASS_NAME, "post-card-inline__title").text
                    url = element.find_element(By.CLASS_NAME, "post-card-inline__title-link").get_attribute("href")
                    datetime = element.find_element(By.CLASS_NAME, "post-card-inline__date").get_attribute("datetime")
                    author = element.find_element(By.CLASS_NAME, "post-card-inline__author").text
                    text = element.find_element(By.CLASS_NAME, "post-card-inline__text").text
                    id = urlparse(url).path

                    single_news = {
                      "urlId": id,
                      "title": title,
                      "url": url,
                      "datetime": datetime,
                      "author": author,
                      "text": text
                    }
                    news.append(single_news)

        finally:
            self.driver.quit()

        return news

    def get_news_single(self, urlId):
        url = "https://cointelegraph.com" + urlId
        self.driver.get(url)

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'post-content')))
            content = self.driver.find_element(By.CLASS_NAME, 'post-content').text

            return content
        except Exception as e:
            print(f"Error al obtener el contenido de la noticia: {e}")
            return None
        finally:
            self.driver.quit()

