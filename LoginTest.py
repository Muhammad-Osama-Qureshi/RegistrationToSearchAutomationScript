from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class LoginTest:
    def loginScreen(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        driver.get("http://localhost/opencart/upload/index.php?route=common/home&language=en-gb")
        driver.find_element(By.XPATH,"//span[normalize-space()='My Account']").click()
        driver.find_element(By.XPATH,"//a[@class='dropdown-item'][normalize-space()='Login']").click()
        email = driver.find_element(By.ID, "input-email")
        email.send_keys("b@gmail.com")
        passw = driver.find_element(By.ID, "input-password")
        passw.send_keys("12345")
        btn = driver.find_element(By.CSS_SELECTOR, "form button")
        btn.click()









