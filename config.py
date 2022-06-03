import sys

selenium_arguments = [
    'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/97.0.4692.99 Safari/537.36',
    '--disable-blink-features=AutomationControlled']


match sys.platform:
    case 'linux':
        browser_path = 'selenium_drivers/'
    case 'darwin': # MAC
        browser_path = 'selenium_drivers/chromedriver_mac'
    case 'win32':
        browser_path = 'drivers/chromedriver.exe'
    case _:
        print("ERROR: can't found selenium driver")

wait_time = 3
