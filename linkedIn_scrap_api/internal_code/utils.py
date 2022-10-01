from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

# assign the chromedriver path
CHROMEDRIVER_PATH = r"D:\chromedriver.exe"


def get_connections_link(start=0):
    if start == 0:
        connections_link = f"https://www.linkedin.com/voyager/api/relationships/dash/connections?decorationId=com.linkedin.voyager.dash.deco.web.mynetwork.ConnectionListWithProfile-15&count=40&q=search&sortType=RECENTLY_ADDED"
    else:
        connections_link = f"https://www.linkedin.com/voyager/api/relationships/dash/connections?decorationId=com.linkedin.voyager.dash.deco.web.mynetwork.ConnectionListWithProfile-15&count=40&q=search&sortType=RECENTLY_ADDED&start={start}"
    return connections_link


def get_required_cookies(user_id_string, password_string):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    browser = webdriver.Chrome(CHROMEDRIVER_PATH, options=chrome_options)

    browser.get("https://www.linkedin.com")
    delay = 3  # seconds
    try:
        # Wait for the page to load
        WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'session_key')))
        WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'session_password')))
        WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'sign-in-form__submit-button')))
    except TimeoutException:
        print("Loading took too much time!")

    # Login with username and password
    username = browser.find_element(By.ID, "session_key")
    username.send_keys(user_id_string)
    password = browser.find_element(By.ID, "session_password")
    password.send_keys(password_string)
    login_button = browser.find_element(By.CLASS_NAME, "sign-in-form__submit-button")
    login_button.click()

    # Gets JSESSIONID and li_at from cookies data
    browser_cookies = browser.get_cookies()
    required_cookies = {
        'JSESSIONID': [el['value'] for el in browser_cookies if el['name'] == 'JSESSIONID'][0].strip('"'),
        'li_at': [el['value'] for el in browser_cookies if el['name'] == 'li_at'][0].strip('"')
    }
    return required_cookies
