from crawl.bacs_crawl import go_to_targeturl
import logging, coloredlogs
from coloredlogs import parse_encoded_styles

logger = logging.getLogger(__name__)

coloredlogs.DEFAULT_LEVEL_STYLES = {'critical': {'color': 'cyan', 'bold': True, 'background': 'red'},
                                    'debug': {'color': 'green'},
                                    'error': {'color': 'red'},
                                    'info': {'color': 'green', 'background': 'black'},
                                    'notice': {'color': 'magenta'},
                                    'spam': {'color': 'green', 'faint': True},
                                    'success': {'color': 'green', 'bold': True},
                                    'verbose': {'color': 'blue'},
                                    'warning': {'color': 'yellow'}}
coloredlogs.install(level='INFO', logger=logger)


