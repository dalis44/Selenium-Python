from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import unittest
import tempfile
from selenium.webdriver.support.ui import Select
class TestLogIn(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        })
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        profile_path = tempfile.mkdtemp()
        chrome_options.add_argument(f"--user-data-dir={profile_path}")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.implicitly_wait(10)

    def test_Dropdown(self):
        driver = self.driver
        dropdown_element = driver.find_element(By.LINK_TEXT, "Dropdown").click()
        MyExplicitWait = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "dropdown")))
        MyExplicitWait.click()
        #dropdown_element1 = driver.find_element(By.ID, "dropdown").click()
        
        select = Select(MyExplicitWait)
        select.select_by_visible_text("Option 1")
        select.select_by_value("2")
        select.select_by_index(0)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
