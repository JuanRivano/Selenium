from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
driverChrome =webdriver.Chrome("C:\\Users\\one21\\PycharmProjects\\selenium\\chromedriver.exe")


def connectChrome(url):
 driverChrome.get(url)
 return driverChrome

