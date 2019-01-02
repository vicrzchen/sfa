from selenium import webdriver
from selenium.webdriver.ie.options import Options
from scrapy_db.constvalue import BROWSER_PATH
from kits.log_kits import logger


def init_new_browser():
    ie_option = Options()
    ie_option.add_argument('--headless')
    ie_option.add_argument('--disable-gpu')
    try:
        browser = webdriver.Ie(BROWSER_PATH)
    except Exception as exceinfo:
        logger.error(exceinfo)
        return None

    return browser
