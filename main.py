from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

#driver = webdriver.Chrome(executable_path=os.popen('which chromedriver').read().strip())
#driver = webdriver.Chrome('/Users/linushenn/Downloads')
driver = webdriver.Chrome(ChromeDriverManager().install())
browser = webdriver.Chrome()

browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title

elem = browser.find_element(By.NAME, 'p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()