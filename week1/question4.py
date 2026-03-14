'''
Open the Myntra website using Selenium WebDriver.
 Locate the search input field on the homepage using the class name locator.
 Enter the text "shoes" into the search field using Selenium’s send_keys() method.

Ensure that the correct locator is used to identify the search box before entering the text.
'''


from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver=Chrome(options=o)
driver.get("https://www.myntra.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.CLASS_NAME , 'desktop-searchBar').send_keys("shoes")
sleep(2)
driver.close()
