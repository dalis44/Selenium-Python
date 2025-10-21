from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import unittest
import tempfile

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
        self.driver.get("http://the-internet.herokuapp.com/dynamic_loading/1")
        self.driver.implicitly_wait(10)

    def test_WaitsInteract(self):
        driver = self.driver
        driver.find_element(By.TAG_NAME, "button").click()
        waitMsg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4"))
        )
        self.assertEqual(waitMsg.text, "Hello World!", "Expected message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
