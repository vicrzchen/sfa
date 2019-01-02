from crawl.bacs_crawl import go_to_targeturl
from kits.log_kits import logger
from kits.browser_kits import init_new_browser

new_browser = init_new_browser()

if new_browser is None:
    logger.warning('Can not initiate a browser')
    exit(-1)

go_to_targeturl(browser=new_browser)
