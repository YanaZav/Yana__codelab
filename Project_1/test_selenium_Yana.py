from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

class GooglePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.google.com/')
        time.sleep(1)

    def accept(self, accept_button):
        self.driver.find_element("id",accept_button).click()  
        time.sleep(1)

    def check_logo_dispayed(self, logo):
        logo_= self.driver.find_element('xpath', logo)
        
        if logo_.is_displayed():
            print("Logo jest wyświetlane na stronie.")
        else:
            print("Logo nie jest wyświetlane na stronie.")

class Search(GooglePage):

    def enter_search_query(self, search_box, query):
        search_box_ = self.driver.find_element('xpath', search_box)
        search_box_.send_keys(query)
        search_box_.send_keys(Keys.ENTER)
        time.sleep(1)

    def get_search_results(self):
        search_results_ = self.driver.find_element('id','search')

        if search_results_.is_displayed():
            print("Wyniki wyszukiwania zostały poprawnie wyświetlone.")
        else:
            print("Wystąpił problem podczas wyświetlania wyników wyszukiwania.")
        
    def go_to_page(self, page):
        page_ = self.driver.find_element('xpath', page).click()
        time.sleep(1)
        

google_page = GooglePage(driver)
search = Search(driver)

# Otwarcie strony Google
google_page.open() 

# Kliknięcie przycisku akceptacji na stronie Google
google_page.accept("L2AGLb") 

# Sprawdzenie, czy wyświetla się logo
print("Test 1: Czy wyświetla się logo Google?")
google_page.check_logo_dispayed('/html/body/div[1]/div[2]/div/img')

# Wpisanie zapytania wyszukiwania
search.enter_search_query('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea','codelab eu')

# # Sprawdzenie, czy wyniki zostały wyświetlone
print("Test 2: Czy wyszukuje 'codelab eu'?")
search.get_search_results()

# Przejście na wybraną stronę
search.go_to_page('//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a/h3')

# Kliknięcie przycisku akceptacji na stronie Codelab.eu
search.accept('wt-cli-accept-all-btn')

# Sprawdzenie, czy wyświetla się logo Codelab
print("Test 3: Czy wyświetla się logo Codelab?")
search.check_logo_dispayed('/html/body/main/section[1]/div/div[2]/div/div[1]/div/div/a/img')

