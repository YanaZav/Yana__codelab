*** Setting ***
Library   kw.py

*** Test Cases ***
Robot First Test Case
    Log   Otwieranie strony "codelab.eu"
    Open Page  https://codelab.eu 
Robot Second Test Case
    Log    Klikniecie przycisku "Services"
    Click Button   https://codelab.eu     /html/body/main/section[1]/div/div[2]/div/div[1]/div/nav/div/ul/li[1]  
Robot Third Test Case 
    Log    Przekierowanie na podstrone "services"
    Verify Redirect   https://codelab.eu     /html/body/main/section[1]/div/div[2]/div/div[1]/div/nav/div/ul/li[1]  https://codelab.eu/en/services