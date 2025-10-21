from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import unittest
from selenium.webdriver.common.keys import Keys

class TestLogIn(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://the-internet.herokuapp.com")
        self.driver.implicitly_wait(10)

    
    def test_LogIn(self):
        driver = self.driver
        btn = driver.find_element(By.LINK_TEXT , "JavaScript Alerts")
        waitMsg = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "heading")))
        print(waitMsg.text)
        btn.click()
        waitMsg = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "h3")))
        element = driver.find_element(By.TAG_NAME, "h3")
        time.sleep(2)
        #element = driver.find_element(By.CSS_SELECTOR, "button[onclick*='jsAlert']")
        #element = driver.find_element(By.XPATH, "//h3[text()='JavaScript Alerts']")
        #element = driver.find_element(By.XPATH, "//h3[contains(text(), 'JavaScript')]")
        #element = driver.find_element(By.CSS_SELECTOR, "button[onclick*='jsAlert']")
        
        button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick='jsAlert()']")))
        button.click()
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        result = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,"result")))
        self.assertIn("You successfully clicked an alert", result.text)
  
        #print(element.text)  
        #time.sleep(10)
        #print(f"Page Title : {driver.title}")
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()