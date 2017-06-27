'''
Created on Jun 27, 2017

@author: NMakkar
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(executable_path="C:\\Users\\nmakkar\\.jenkins\\workspace\\Coax-mercury\\src\\main\\resources\\Drivers_executable\\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\\Users\\nmakkar\\Documents\\My Received Files\\geckodriver-v0.13.0-win64\\geckodriver.exe");
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()