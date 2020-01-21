from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome("chromedriver")

browser.maximize_window()

browser.get("https://www.bongobd.com/")
timeout = 5
try:
    television_selector = "a[href='/channel/channel-24']"
    # television_selector = ".jss1326"

    element_present = EC.presence_of_element_located(
        (By.CSS_SELECTOR, television_selector))
    WebDriverWait(browser, timeout).until(element_present)
    elements = browser.find_elements_by_css_selector(television_selector)
    elements[0].click()
except TimeoutException:
    print("Timed out waiting for page to load")
