'''
Description
Open the Naukri.com website using Selenium WebDriver.
 Navigate to the registration page and identify the text input fields such as Name, Email, and Password.

Use the ID locator strategy to locate these elements and enter appropriate sample data into each field using Selenium commands.

Students should ensure that the browser opens successfully, elements are identified correctly, and the values are entered into the fields.
'''

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver=Chrome(options=o)
driver.get("https://www.naukri.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.LINK_TEXT , "Register").click()
sleep(2)
driver.find_element(By.ID, "name").send_keys("Akshita Agarwal")
sleep(2)
driver.find_element(By.ID, "email").send_keys("akshita@gmail.com")
sleep(2)
driver.find_element(By.ID, "password").send_keys("akshita")
sleep(2)
driver.close()