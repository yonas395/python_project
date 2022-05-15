from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\chromedriver.exe")
driver.get("https://www.amazon.com/")

# Amazon logo = by.id
driver.find_element(By.ID, 'logo-sprites')

# sign in = by.XPATH
driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")

# continue button = by 2 attribute 'and'
driver.find_element(By.XPATH, "//input[@id='continue' and @class='a-button-input']")

# need help = by.XPath, partial contain
driver.find_element(By.XPATH, "//span[contains(@class,'a-expander-prompt')]")


# conditions of use and privacy = by.partial attribute
driver.find_element(By.XPATH, "//a[contains(@href, 'signin_notification_condition_of_use')]")


# email = by.text
driver.find_element(By.XPATH,"//a[text()='Best Sellers' and @href='bestsellers']")

#  forgot password =  By XPath, only attribute or text, no tag

#  other issues with sign-in = # By XPath, using multiple nodes

# creat your amazon account = by.partial attribute



