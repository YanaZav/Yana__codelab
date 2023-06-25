from selenium import webdriver
driver = webdriver.Chrome()

#Keyword Open Page  
def open_page(url):
    driver.get(url)
    driver.maximize_window()
    
#Keyword Click Button
def click_button(url,xpath_button):
    open_page(url)  
    driver.find_element('xpath',xpath_button).click()

#Keyword Verify Redirect
def verify_redirect(url, button_xpath, expected_url):
    click_button(url, button_xpath)
    current_url = driver.current_url
    assert current_url == expected_url 
    

