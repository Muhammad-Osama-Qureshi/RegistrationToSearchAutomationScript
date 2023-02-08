import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Register:
    def RegisterScreen(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        driver.get("http://localhost/opencart/upload/index.php?route=common/home&language=en-gb")
        driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
        driver.find_element(By.XPATH,"//a[@class='dropdown-item'][normalize-space()='Register']").click()
        driver.find_element(By.XPATH,"//input[@id='input-firstname']").send_keys("Osama")

        driver.find_element(By.XPATH,"//input[@id='input-lastname']").send_keys("Qureshi")
        driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys("z@gmail.com")
        driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("wwwwdasd")
        driver.execute_script("window.scrollBy(0,925)", "")
        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR,"#input-newsletter-yes").click()
        driver.find_element(By.XPATH,"//input[@name='agree']").click()
        driver.find_element(By.XPATH,"//button[normalize-space()='Continue']").click()
        time.sleep(4)
        driver.find_element(By.XPATH,"//a[normalize-space()='Continue']").click()
        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("MacBook")
        driver.find_element(By.XPATH,"//button[@class='btn btn-light btn-lg']").click()
        driver.find_element(By.XPATH,"//img[@title='MacBook']").click()
        driver.find_element(By.XPATH,"//button[@id='button-cart']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//button[normalize-space()='1 item(s) - $602.00']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//strong[normalize-space()='View Cart']").click()
        driver.execute_script("window.scrollBy(0,925)", "")
        time.sleep(2)
        driver.find_element(By.XPATH,"//a[@class='btn btn-primary']").click()




