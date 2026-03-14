'''
Open the YouTube website using Selenium WebDriver.
 Locate the search input field on the homepage and enter the text "melody hits" into the search box.

Use Selenium’s send_keys() method to type the text into the search field.


'''




from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver=Chrome(options=o)
driver.get("https://www.youtube.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.NAME , "search_query").send_keys("melody hits")
sleep(2)
driver.close()
