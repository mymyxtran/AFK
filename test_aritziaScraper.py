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

class TestAritziaScraper():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_aritziaScraper(self):
    self.driver.get("https://www.aritzia.com/en/home")
    self.driver.set_window_size(784, 864)
    self.driver.find_element(By.LINK_TEXT, "Clothing").click()
    self.driver.find_element(By.CSS_SELECTOR, ".active > .refinement-link-text").click()
    self.driver.execute_script("window.scrollTo(0,192)")
    self.driver.find_element(By.CSS_SELECTOR, ".ar-product-grid__tile:nth-child(1) .product-image .lazy").click()
    # Product Name
    self.driver.find_element(By.CSS_SELECTOR, ".pdp-product-name__name:nth-child(1)").click()
    # Product Description
    self.driver.find_element(By.CSS_SELECTOR, ".pdp-product-name > .pdp-product-name__subtitle").click()
    # Price
    self.driver.find_element(By.CSS_SELECTOR, ".price-default > span").click()
    self.driver.find_element(By.LINK_TEXT, "Details").click()
    # Material Content
    self.driver.find_element(By.CSS_SELECTOR, ".js-product-accordion__content:nth-child(4) li:nth-child(1)").click()
    # Scrape all details
    self.driver.find_element(By.ID, "pdp-panel-stuck").click()
    # Fetch Class to get rating
    self.driver.find_element(By.CSS_SELECTOR, ".js-pdp-accordian-reviews__tab-trigger > .TTratingBox").click()
  
