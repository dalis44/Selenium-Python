
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestJSAlerts(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        # If you ever run headless, use the new headless:
        # chrome_options.add_argument("--headless=new")
        # On some Windows/GPU combos, this helps:
        # chrome_options.add_argument("--disable-gpu")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(0)  # prefer explicit waits
        self.driver.get("https://the-internet.herokuapp.com")

    def test_click_first_js_alert_button(self):
        driver = self.driver

        # 1) Go to the JavaScript Alerts page
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "JavaScript Alerts"))
        ).click()

        # 2) Ensure we navigated and the correct heading is visible
        WebDriverWait(driver, 10).until(EC.url_contains("/javascript_alerts"))
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h3[normalize-space()='JavaScript Alerts']"))
        )

        # 3) Locate the first button and click it
        #    (the first button is the simple alert: onclick="jsAlert()")
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick='jsAlert()']"))
        )
        # Make sure it’s in view (sometimes needed on small windows)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)

        try:
            button.click()
        except Exception as e:
            # Fallback in case a native click is intercepted
            driver.execute_script("arguments[0].click();", button)

        # 4) Wait for the alert, read and accept it
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        print("Alert text:", alert.text)  # Expected: "I am a JS Alert"
        alert.accept()

        # 5) Verify the result message on the page
        result = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, "result"))
        )
        print("Result text:", result.text)
        self.assertIn("You successfully clicked an alert", result.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
