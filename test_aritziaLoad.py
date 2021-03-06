# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAritziaLoad():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_aritziaLoad(self):
    self.driver.get("https://www.aritzia.com//en/clothing/blouses?lastViewed=109")
    self.driver.set_window_size(786, 864)
    self.driver.execute_script("window.scrollTo(0,9096)")
    # Click Show More
    self.driver.find_element(By.XPATH, "//span[contains(.,\'Show More\')]").click()
    # Click On Image
    self.driver.find_element(By.CSS_SELECTOR, ".ar-product-images__image").click()
  
