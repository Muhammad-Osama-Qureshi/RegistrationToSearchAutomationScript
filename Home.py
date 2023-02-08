from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Home:
    def Home(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        driver.get("http://localhost/opencart/upload/index.php?route=common/home&language=en-gb")