# Generated by Selenium IDE
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common import exceptions as SExceptions
from webdriver_manager.chrome import ChromeDriverManager
from collections import defaultdict
import pandas as pd
PRICE = "price"
SHORT_DESCRIPTION = "short_description"
IMG_SOURCE = "image_source"
GENERAL_DESCRIPTION = "general_description"
SIZE = "size"
MATERIAL = "material"
MANUFACTURER_LOCATION = "manufacturer_location"
MANUFACTURER_NAME = "manufacturer_name"
MANUFACTURER_ADDRESS = "manufacturer_address"
MANUFACTURER_NUM_WORKERS = "manufacturer_num_workers"
BRAND = "brand"
COLOR = "color"

class StoreScraper():
  def __init__(self, DEBUG):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.vars = {}
    self.dict_for_csv = defaultdict(list)
    self.finish = False
    self.DEBUG = DEBUG
  
  def teardown(self):
    self.driver.quit()

  def test_length(self, dictionary : dict):
    for k,v in dictionary.items():
      print("Column %s has %d rows" % (k, len(v)))

  def test_loadMoreHnM(self) -> bool:
    '''
      Description: Check if there exists a 'Load More Button'. If it doesn't exist,
      finish the program and write out the dataframe.
    '''
    # self.driver.get("https://www2.hm.com/en_ca/divided/shop-by-product/shirts-and-blouses.html")
    try:
      self.driver.find_element(By.XPATH, "//div[3]/div[2]/button").click()
    except Exception as e:
      ## If load more doesn't exist, we finish the program
      return True
    
    return False
  
  def look_for_close_HnM(self):
    try:
      close = self.driver.find_element(By.CSS_SELECTOR, ".close")## look for any close signs
      if close == None:
        return
      else:
        close.click()
    except (SExceptions.NoSuchElementException, SExceptions.ElementNotInteractableException) as e:
      pass
    
  def test_tryHMScraper(self, category="Shirts & Blouses"):
    self.dict_for_csv.clear()

    ## Navigation
    self.driver.get("https://www2.hm.com/en_ca/index.html")
    self.driver.set_window_size(782, 871)
    time.sleep(0.5)
    self.driver.find_element(By.CSS_SELECTOR, ".menu__trigger").click()
    time.sleep(0.5)
    self.driver.find_element(By.LINK_TEXT, "Divided").click()
    self.driver.execute_script("window.scrollTo(0,1096.800048828125)")
    time.sleep(0.5)
    self.driver.find_element(By.LINK_TEXT, category).click()
    time.sleep(0.5)
    
    i = 1
    finished = False
    while not finished:
      ## In DEBUG, quit after we scraped two items
      if self.DEBUG:
        if i == 67: 
          break

      try:
        self.driver.find_element(By.CSS_SELECTOR, ".product-item:nth-child(%d) .item-image" % (i)).click()
        time.sleep(1)
      except SExceptions.NoSuchElementException as e:
        finished = self.test_loadMoreHnM()
        continue ## If we finished, export csv. If not finished, keep going
        
      # self.dict_for_csv["imageSrc"].append(image.get_attribute("src"))
      
      # Price
      price = self.driver.find_element(By.CSS_SELECTOR, ".ProductPrice-module--productItemPrice__2i2Hc > span")
      self.dict_for_csv[PRICE].append(price.text)

      # Short Description
      title = self.driver.find_element(By.CSS_SELECTOR, ".primary.product-item-headline")
      self.dict_for_csv[SHORT_DESCRIPTION].append(title.text)

      # Color
      label = self.driver.find_element(By.CSS_SELECTOR, ".product-input-label")
      self.dict_for_csv[COLOR].append(label.text)

      # Image Link
      image = self.driver.find_element(By.CSS_SELECTOR, ".product-detail-main-image-container > img")
      self.dict_for_csv[IMG_SOURCE].append(image.get_attribute("src"))

      # General Description
      general_desc = self.driver.find_element(By.CSS_SELECTOR, ".pdp-description-text")
      self.dict_for_csv[GENERAL_DESCRIPTION].append(general_desc.text)

      general_list = self.driver.find_element(By.CSS_SELECTOR, ".pdp-description-list")
      
      if "Fit" not in general_list.text and "Composition" not in general_list.text:
        self.dict_for_csv[SIZE].append(None)
        self.dict_for_csv[MATERIAL].append(None)
      else:
        ## At least one of these must be non-null. Identify one that is null
        if "Fit" in general_list.text: 
          for entry in general_list.text.split("\n"):
            if "Fit" in entry:
              self.dict_for_csv[SIZE].append(entry)
              break
        else:
          self.dict_for_csv[SIZE].append(None)
        
        if "Composition" in general_list.text:
          for entry in general_list.text.split("\n"):
            if "Composition" in entry:
              self.dict_for_csv[MATERIAL].append(entry)
              break
        else:
          self.dict_for_csv[MATERIAL].append(None)
      
      self.look_for_close_HnM() ## make sure that nothing is obstructing the view of the button we are about to click on

      self.driver.find_element(By.CSS_SELECTOR, ".js-open-sustainability").click()
      time.sleep(1)
      self.driver.find_element(By.CSS_SELECTOR, ".CTA-module--iconPosition-end__Q9WNd").click()
      
      time.sleep(0.5)
      
      # Country of Manufacture
      country = self.driver.find_element(By.CSS_SELECTOR, ".ProductBackground-module--supplierInfoCountry__14s8D > .Heading-module--general__3HQET")
      self.dict_for_csv[MANUFACTURER_LOCATION].append(country.text)
    
      # Manufacture Name
      manufacture_name = self.driver.find_element(By.XPATH, "//div[2]/div/div[3]/div/article/div/div/button")
      self.dict_for_csv[MANUFACTURER_NAME].append(manufacture_name.text)
      manufacture_name.click()
      time.sleep(0.5)

      # Manufacturer Address
      manufacture_address = self.driver.find_element(By.CSS_SELECTOR, ".ProductBackground-module--factories__h_ikg > .BodyText-module--general__32l6J")
      self.dict_for_csv[MANUFACTURER_ADDRESS].append(manufacture_address.text)

      # Number of Workers
      num_workers = self.driver.find_element(By.CSS_SELECTOR, "dl > dd")
      self.dict_for_csv[MANUFACTURER_NUM_WORKERS].append(num_workers.text)
      self.dict_for_csv[BRAND].append("H&M")
      i += 1
      self.driver.execute_script("window.history.go(-1)")

    self.test_length(self.dict_for_csv)
    HnMInfo = pd.DataFrame(self.dict_for_csv)
    HnMInfo.to_csv("./data/HnM_%s.csv" % category.replace(" ", "_"), index=False)

  def test_loadMoreAritzia(self) -> bool:
    # self.driver.get("https://www.aritzia.com/en/clothing/blouses?lastViewed=37")
    try:
      self.driver.find_element(By.CSS_SELECTOR, ".js-load-more__button").click()
    except SExceptions.NoSuchElementException as e:
      ## If load more doesn't exist, we finish the program
      return True
    
    return False
  
  def look_for_close_Aritzia(self):
     ActionChains(self.driver).send_keys(Keys.ESCAPE).perform() ## Get rid of any unwanted banners that pop up
    
  def test_aritziaScraper(self, category="blouses"):
    '''
      Category could be Blouses or T-shirts for now
    '''
    self.dict_for_csv.clear()
    self.driver.get("https://www.aritzia.com/en/clothing/%s" % category)
    
    #######################################################  NAVIGATION  ######################################################################
    self.driver.set_window_size(784, 864)

    # self.driver.find_element(By.XPATH, "//span[contains(.,\'%s\')]" % category)
   
    i = 1
    finished = False
    while not finished:
      temp = self.dict_for_csv
      if self.DEBUG:
        if i == 67: 
          break
      
      time.sleep(2)
      self.look_for_close_Aritzia()
      self.driver.execute_script("window.scrollTo(0,192)")
      time.sleep(0.5)

      try: 
        tile = self.driver.find_element(By.CSS_SELECTOR, ".ar-product-grid__tile:nth-child(%d)" % i)
        imageSrc = tile.find_element(By.CSS_SELECTOR, "img").get_attribute("src") ## This is just to make sure if click happens and causes exception,
        # That we don't end up creating an uneven pandas table  
        tile.click()
        self.dict_for_csv[IMG_SOURCE].append(imageSrc)
        time.sleep(0.5) ## standard wait after clicking to let web page load accordingly
      except SExceptions.NoSuchElementException as e:
        try:
          ga_promotions = self.driver.find_element(By.CSS_SELECTOR, ".ga-promotions.ar-product-grid__tile:nth-child(%d)" % i)
          if ga_promotions != None:
            i += 1
            self.doct_for_csv = temp
            continue
        except SExceptions.NoSuchElementException as e:
          self.dict_for_csv = temp
          finished = self.test_loadMoreAritzia()
          continue
      
      ## If missing any, there is empty page
      try: 
        # Material and Origin Content. This comes first because any other irrelevant page will not have this
        details = self.driver.find_element(By.CSS_SELECTOR, "#pdp-details .ar-pdp-tab-label")
        self.driver.execute_script("arguments[0].click()", details) ## We use javascript click just in case if Aritzia gives us the overlapping shade of death
        time.sleep(0.5)
        description = self.driver.find_element(By.CSS_SELECTOR, ".js-product-accordion__content:nth-child(4)")
        
        if "Origin" not in description.text and "Content" not in description.text:
          self.dict_for_csv[MANUFACTURER_LOCATION].append(None)
          self.dict_for_csv[MATERIAL].append(None)
        else:
          ## At least one existing field
          if "Origin" in description.text:
            for entry in description.text.split("\n"):
              if "Origin" in entry:
                self.dict_for_csv[MANUFACTURER_LOCATION].append(entry)
                break
          else:
            self.dict_for_csv[MANUFACTURER_LOCATION].append(None)

          if "Content" in description.text:
            for entry in description.text.split("\n"):
              if "Content" in entry:
                self.dict_for_csv[MATERIAL].append(entry)
                break
          else:
            self.dict_for_csv[MATERIAL].append(None)
          
        # Product Description
        description = self.driver.find_element(By.CSS_SELECTOR, ".pdp-product-name > .pdp-product-name__subtitle")
        self.dict_for_csv[SHORT_DESCRIPTION].append(description.text)
        
        # Price
        price = self.driver.find_element(By.CSS_SELECTOR, ".price-default")
        self.dict_for_csv[PRICE].append(price.text)

        self.dict_for_csv[GENERAL_DESCRIPTION].append(description.text)

        # Find Color and Size
        colors = []
        color_header = self.driver.find_element(By.CSS_SELECTOR, ".swatches-color")
        colors = color_header.text ## Combine colors back to string

        ## Add colors to general description
        self.dict_for_csv[COLOR].append(colors)

        sizes = []
        size_header = self.driver.find_element(By.CSS_SELECTOR, ".swatches-size")
        sizes = size_header.text
        
        self.dict_for_csv[SIZE].append(sizes)
        self.dict_for_csv[BRAND].append("Aritzia")
      except SExceptions.NoSuchElementException as e:
        self.dict_for_csv = temp
        pass
      i += 1
      self.driver.execute_script("window.history.go(-1)")
      # Fetch Class to get rating. NOT IMPLEMENTED FOR NOW
      # self.driver.find_element(By.CSS_SELECTOR, ".js-pdp-accordian-reviews__tab-trigger > .TTratingBox").click()
    
    self.test_length(self.dict_for_csv)
    AritiziaInfo = pd.DataFrame(self.dict_for_csv)
    AritiziaInfo.to_csv("./data/AritizaInfo_%s.csv" % category, index=False)  
      