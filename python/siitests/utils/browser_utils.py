import chromedriver_binary # Importing this exports chrome path to $PATH, below code will fail without this import
from selenium import webdriver


def setup_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    return webdriver.Chrome(chrome_options=chrome_options)