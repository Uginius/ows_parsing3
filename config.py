import sys


wait_time = 5

match sys.platform:
    case 'linux':
        browser_path = 'drivers/chromedriver_linux64_99.0.4844.51/chromedriver'
        user_agent = None
    case 'darwin':
        browser_path = 'drivers/chromedriver'
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    case 'win32':
        browser_path = 'drivers/chromedriver.exe'
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    case _:
        print("ERROR: can't found selenium driver")
        user_agent = None

selenium_arguments = [f'user-agent={user_agent}', '--disable-blink-features=AutomationControlled']
req_headers = {'accept': '*/*', 'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 'user-agent': user_agent}
