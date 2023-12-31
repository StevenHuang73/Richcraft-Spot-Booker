from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pause
from datetime import datetime
import sys
import time
from getcode import get_code

# Headless option, might not work
chrome_options = Options()
chrome_options.add_argument("--headless")

email_address = "<EMAIL>"
email_password = "<PASSWORD>"

def register(name1, phone1, date, time1, program, spots, location):
    browser = webdriver.Chrome()
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    print(currentYear,currentMonth,currentDay)
    for y in range(5):
        try:
            browser.get(location)
            pause.until(datetime(currentYear, currentMonth, currentDay, hour=18, minute=0, second=0))

            browser.find_element(by=By.LINK_TEXT, value=program).click()
            number = browser.find_element(by=By.XPATH, value='//*[@id="reservationCount"]')
            number.clear() 
            number.send_keys(spots)
            browser.find_element(by=By.XPATH, value='//*[@id="submit-btn"]/span').click()
            browser.find_element(by=By.LINK_TEXT, value=date).click()
            string = "'" + time1 + " " + date + "'"
            print(string)
            browser.find_element(by=By.XPATH, value = "//a[@aria-label="+string+"]").click()
            phone_number = browser.find_element(by=By.XPATH, value='//*[@id="telephone"]')
            phone_number.clear()
            phone_number.send_keys(phone1)
            email = browser.find_element(by=By.XPATH, value='//*[@id="email"]')
            email.clear()
            email.send_keys(email_address)
            # name = browser.find_element(by=By.XPATH,value='//*[@id="field2065"]') //*[@id="mainForm"]/div[2]/div/div[4]/div[1]/label/span
            # (xpath = "//*[contains(text(), 'Best Choice')]")

            name_parent = browser.find_element(by=By.XPATH, value='//*[@id="mainForm"]/div[2]/div/div[4]/div[1]/label')
            name = name_parent.find_element(by=By.TAG_NAME, value='input')
            name.clear()
            name.send_keys(name1)

            time.sleep(0.5)
            browser.find_element(by=By.XPATH, value='//*[@id="submit-btn"]/span').click()

            for x in range(10):
                try:
                    time.sleep(2)
                    x = get_code(email_address,email_password,'imap.gmail.com')
                    if(len(x) == 4):
                        break
                    time.sleep(0.3)
                except:
                    print("error_get_code")


            print(x)
            number = browser.find_element(by=By.XPATH, value='//*[@id="code"]')
            number.send_keys(x)
            time.sleep(1)
            browser.find_element(by=By.XPATH, value='//*[@id="mainForm"]/div/div/button/span').click()
            time.sleep(1)
            browser.quit
            return("Success")
        except Exception as e:
            print("error", e)
            
        return("Fail")


