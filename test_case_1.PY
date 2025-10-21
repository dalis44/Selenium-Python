import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import tempfile

class TestLogIn(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
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

        # Use a temporary profile to avoid session errors
        profile_path = tempfile.mkdtemp()
        chrome_options.add_argument(f"--user-data-dir={profile_path}")

        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://the-internet.herokuapp.com/login")

    def test_LogIn(self):
        driver = self.driver

        # Fill in login form
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, ".radius").click()

        # Wait for login message
        flash_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )
        print(f"Login Message: {flash_msg.text.strip()}")

        # Validate login success
        self.assertIn("You logged into a secure area!", flash_msg.text)

        # Validate logo presence
        logo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "img"))
        )
        src_val = logo.get_attribute("src")
        print(f"Logo source: {src_val}")
        self.assertTrue(src_val.startswith("http"))

        # Validate page title
        self.assertEqual(driver.title, "The Internet")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()