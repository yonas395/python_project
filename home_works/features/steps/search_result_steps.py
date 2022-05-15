from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

F_ITEM = (By.XPATH, "//span[@class='a-price-whole']")
CART = (By.ID, 'add-to-cart-button')
BB_SEARCH = (By.ID, 'twotabsearchtextbox')

@when('click on {search_word}')
def click_first_result(context, search_word):
    context.driver.find_element(*BB_SEARCH).send_keys('basketball', Keys.ENTER)
    context.driver.find_element(*F_ITEM).click()
    context.driver.find_element(*CART).click()
    sleep(2)