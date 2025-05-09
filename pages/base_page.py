from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def is_visible(self, xpath: str) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return True
        except Exception:
            return False

    def is_clickable(self, xpath: str) -> bool:
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            return True
        except Exception:
            return False

    def click(self, xpath: str) -> None:
        self.wait_for_overlay_to_disappear()
        element = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        if self.is_clickable(xpath):
            element.click()

    def get_text(self, xpath: str) -> str:
        if self.is_visible(xpath):
            return self.driver.find_element(By.XPATH, xpath).text.strip()
        return ""

    def send_keys(self, xpath: str, text: str) -> None:
        if self.is_visible(xpath):
            element = self.driver.find_element(By.XPATH, xpath)
            element.clear()
            element.send_keys(text)

    def wait_for_overlay_to_disappear(self, xpath: str = "//div[contains(@class, 'Splash_container__')]") -> None:
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, xpath))
            )
        except Exception:
            pass
