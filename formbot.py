from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://etickets.theacropolismuseum.gr')

def clickbutton(id):
    driver.find_element(By.ID, id).click()

def clickcheckbox(path):
    driver.find_element(By.XPATH, path).click()

def wait(time, path):
    try:
        WebDriverWait(driver, time).until(EC.presence_of_element_located([By.XPATH, path]))
    finally:
        driver.execute_script("window.scrollTo(0,400)")

def intro():
    lang = driver.find_element(By.CLASS_NAME, 'intro_gr')
    lang.click()
    print("clicked")

    clickbutton('toStep3')
    print("next clicked")

def datemodification():
    today = date.today()
    d = today.strftime("%d")
    print(d)
    datemodified = today.replace(day=int(d)+3)
    datemodified = str(datemodified)
    print(datemodified)
    return datemodified

def selectdatetime(modified_date):
    #pairnei oles tis meres poy einai diathesimes na epilextoyn kai dialegei thn modified h opoia einai 3 meres meta th shmerinh
    alldates = driver.find_elements(By.XPATH, "//div[@class='pignose-calendar-body']//div[contains(@class,'pignose-calendar-unit-date') and not(contains(@class,'pignose-calendar-unit-disabled'))]")
    for date in alldates:
        if date.get_attribute("data-date") == modified_date:
            date.click()
            print("date clicked")
            break

    selecthours = driver.find_element(By.XPATH, "//*[@id='hours_in']/button[3]")
    selecthours.click()
    print("hours clicked")

    clickbutton('toStep4')
    print("next clicked")

def addpersons():
    #time.sleep(1)
    ticketsplus = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='step_4']/div[3]/div[2]")))
    ticketsplus.click()
    print("one more person added")

    driver.execute_script("window.scrollTo(0,400)")

    driver.find_element(By.XPATH, "//*[@id='chooseLanguageSelect']/option[38]").click()
    print("language clicked")

    clickbutton('toStep5')
    print("next clicked")
    

def fill_out_form():
    fields = {  'OrderFirstname' : 'GGGGG',
            'OrderLastName'  : 'SSSSSS',
            'OrderAddress'  : 'MMMMMMMM 30',
            'OrderPostalCode': '11111',
            'OrderCity': 'Thessaloniki',
            'OrderCountryId' : 'Greece',
            'OrderEmail' : 'gst@gmail.com',
            'OrderEmailConfirmation' : 'gst@gmail.com',
            'OrderPhoneNumber' : '6999999999'  }

    for name, value in fields.items():
        element = driver.find_element(By.NAME, name)
        if name == 'OrderCountryId':
            for option in element.find_elements(By.TAG_NAME , 'option'):
                if option.text == value:
                    option.click()
                    break
        else:
            element.send_keys(value)


def accept_terms():
    driver.execute_script("window.scrollTo(0,400)")

    driver.find_element(By.CLASS_NAME, 'iti__selected-flag').click()

    targetcountry = driver.find_element(By.XPATH,"//ul[@class='iti__country-list']/li[@data-country-code='gr']")
    driver.execute_script("arguments[0].scrollIntoView();", targetcountry)
    targetcountry.click()

    clickcheckbox('//*[@id="orderFrm"]/div[10]/input')
    clickcheckbox('//*[@id="orderFrm"]/div[11]/input')

    

if __name__ == '__main__':
    intro()
    modified_date = datemodification()
    #time.sleep(2)
    wait(20, '//*[@id="step_3"]/div[3]/div[2]/div[1]')
    selectdatetime(modified_date)
    #time.sleep(1)

    addpersons()

    wait(20, "//*[@id='orderFrm']")

    fill_out_form()
    accept_terms()
    clickbutton("toBank")


