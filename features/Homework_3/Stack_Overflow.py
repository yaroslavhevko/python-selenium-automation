from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from sample_script import driver_path

driver_path = ChromeDriverManager().install()
#Start Chrome browser:
service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

# Open stackoverflow.com/user/signup
driver.get("https://stackoverflow.com/users/signup")



#Locators

#For Create your account
driver.find_element(By.XPATH, "//h1[text()='Create your account']")

#For text By clicking...
driver.find_element(By.XPATH, "//div[@class='flex--item js-terms fs-caption fc-black-400 ta-left']")

#For Email
driver.find_element(By.ID, 'email')

#For Password
driver.find_element(By.ID, 'password')

#For Show password button
driver.find_element(By.XPATH, "//svg[contains(@class,'js-show-password')]").click()

#For Sign up button
driver.find_element(By.ID, 'submit-button').click()

#For Sign Up with Google
driver.find_element(By.XPATH, "//button[@data-provider='google']").click()

#For Sign Up with GitHub
driver.find_element(By.XPATH, "//button[@data-provider='github']").click()

#For link text Get Stack Overflow...
driver.find_element(By.XPATH, "//a[contains(@href,'stackoverflow.com/teams')]").click()

