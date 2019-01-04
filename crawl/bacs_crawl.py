from selenium.webdriver.common.keys import Keys
from scrapy_db.constvalue import STARTUP_URL
from selenium.webdriver import Ie
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from kits.log_kits import logger
from selenium.webdriver.common.alert import Alert

# 打开到目标地址
def go_to_target_url(browser=None):
    browser = login_sfa(browser=browser)
    browser = go_to_target_area(browser=browser)
    browser = bacs_search_all(browser=browser)
    browser.switch_to.frame(0)
    browser.switch_to.frame('MainWindow')
    return browser


def go_to_target_area(browser=None):
    if browser is not None:
        browser.switch_to.frame(0)
        browser.switch_to.frame('leftFrame')
        browser.find_elements_by_id('treeMenu_110_a')[0].click()
        browser.find_elements_by_id('treeMenu_139_a')[0].click()
        browser.find_elements_by_id('treeMenu_140_a')[0].click()
        browser.find_elements_by_id('treeMenu_141_a')[0].click()
        browser.switch_to.parent_frame()
        browser.switch_to.frame('MainWindow')
        return browser
    return None


def bacs_search_all(browser=None):
    if browser is not None:
        main_window_handle = browser.current_window_handle
        browser.find_element_by_id('ctl00_BtnSearch').click()
        select_expense_type_handle = None
        while not select_expense_type_handle:
            for handle in browser.window_handles:
                if handle != main_window_handle:
                    select_expense_type_handle = handle
                    break
        browser.switch_to.window(select_expense_type_handle)
        browser.switch_to.frame('DialogWindow')
        browser.find_element_by_id('ctl00_C1_ctl00_DdlStatus').send_keys(Keys.ARROW_UP)
        browser.find_element_by_id('ctl00_C2_BtnOK').click()
        browser.switch_to.window(main_window_handle)
        return browser
    return None


def login_sfa(browser:Ie =None):
    if browser is not None:
        browser.get(STARTUP_URL)
        browser.get("javascript:document.getElementById('overridelink').click();")
        browser.find_element_by_id('L1_LoginButtonDomain').click()
        return browser
    return None

