from selenium import webdriver


def setup_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    return webdriver.Chrome(r"C:\Users\UQ58VJ\ProcesDevel\chromedriver_win32\chromedriver.exe", chrome_options=chrome_options)