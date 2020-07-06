import selenium
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.onecountry.com/giveaways/give-million-cash-entry/")
assert 'Country' in driver.title
elemNameOne = driver.find_element_by_name('first_name')
elemNameOne.clear()
elemNameOne.send_keys('James')
elemNameOne.send_keys(Keys.RETURN)


