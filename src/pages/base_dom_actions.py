from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""
This class is a wrapper for selenium webdriver.
"""


class DomActions:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        """
        Clicks on an element identified by locator.
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def enter_text(self, locator, text):
        """
        Enters text in an element identified by locator.
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        Returns text of an element identified by locator.
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text

    def is_element_present(self, locator):
        """
        Returns True if element is present in DOM.
        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except BaseException:
            return False

    def is_element_visible(self, locator):
        """
        Returns True if element is visible in DOM.
        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except BaseException:
            return False

    def is_element_clickable(self, locator):
        """
        Returns True if element is clickable in DOM.
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            return True
        except BaseException:
            return False

    def wait_for_element(self, locator):
        """
        Waits for an element to be present in DOM.
        """
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def force_click_element(self, locator):
        """
        Clicks on an element identified by locator.
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].click();", element)
