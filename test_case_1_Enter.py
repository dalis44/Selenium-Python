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
        self.driver.get("https://the-internet.herokuapp.com/login")
        self.driver.implicitly_wait(10)

    
    def test_LogIn(self):
        driver = self.driver
        un = driver.find_element(By.ID , "username")
        un.clear()
        un.send_keys("tomsmith")
        
        psw = driver.find_element(By.ID , "password")
        psw.clear()
        psw.send_keys("SuperSecretPassword!")
        un.send_keys(Keys.RETURN)
    


        #driver.find_element(By.CLASS_NAME , "radius").click()
        #driver.find_element(By.TAG_NAME , "button").click()
        #driver.find_element(By.CSS_SELECTOR , ".radius").click()
        #driver.find_element(By.CSS_SELECTOR, "button.radius").click()
        #time.sleep(3)

        time.sleep(3)
        print(f"Page Title : {driver.title}")
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()