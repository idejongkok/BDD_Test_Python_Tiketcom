from behave import *
from selenium import webdriver
import time


@given('launch Chrome browser')
def openbrowser(context):
    context.driver= webdriver.Chrome('C:\driver\chromedriver\chromedriver.exe')


@when('Open Tiket.com homepage')
def openhomepage(context):
    context.driver.get('https://www.tiket.com/')
    context.driver.implicitly_wait(10)

    Blocker = context.driver.find_elements_by_xpath('//*[@id="ab-iam-0852068100e25b53bf268f196f732e8a"]/div[2]/button')
    if len(Blocker) == 1:
        context.driver.find_element_by_xpath('//*[@id="ab-iam-0852068100e25b53bf268f196f732e8a"]/div[2]/button').click()
    else:
        pass
    context.driver.implicitly_wait(5)


@when('Select "Kereta Api" Menu')
def selectmenu(context):
    context.driver.find_element_by_link_text('Kereta Api').click()
    context.driver.implicitly_wait(5)


@when('Select Origin Station')
def origin(context):
    context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/input').click()
    context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/ul/li[5]/div[2]/div[2]').click()


@when('Select Destination')
def destination(context):
    context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[2]/div[3]/div[2]/div[2]/div/input').click()
    context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div[2]/ul/li[1]/div[2]/div[1]').click()


@when('Select Departure Time')
def departuretime(context):
    context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[2]/div[4]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td[7]/div').click()


@when('Set 3 Adults & 2 infants pax')
def setpax(context):
    context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[2]/div[6]/div[2]/div/input').click()

    for adult in range(2):
        context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[2]/div[6]/div[2]/div/div/div[2]/div[1]/div[2]/div[3]/button/i').click()

    for infant in range(2):
        context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[2]/div[6]/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button/i').click()

    context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[2]/div[6]/div[2]/div/div/div[3]/button').click()

@when('Press Search Button')
def searchtrain(context):
    context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[3]/button').click()
    #context.driver.set_page_load_timeout(20)
    time.sleep(5)

@when('Select Train Class, Time departure, Train name')
def filtertrain(context):
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div/div[3]/div').click()
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div').click()
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/div[2]/div/div[3]/div[2]/div/div[1]/div').click()
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/button').click()
    context.driver.set_page_load_timeout(20)
    time.sleep(5)

@when('Input Pax Data')
def paxdata(context):

    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[1]/div/input').click()
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[1]/div/div[3]/ul/li[1]').click()

    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[2]/div/input').send_keys('Passenger Test One')
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[3]/div[2]/div/input').send_keys('passenger@gmail.com')
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[3]/div[3]/div[2]/div/input').send_keys('08120000000')

    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/label/div').click()

    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[4]/div/input').send_keys('1000000000')

    #penumpang2
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div/input').click()
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/ul/li[2]').click()
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[3]/div[3]/div/input').send_keys('Passenger Test Two')
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[3]/div[4]/div/input').send_keys('2000000000')

    #penumpang3
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[4]/div[2]/div/input').click()
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[4]/div[2]/div/div[3]/ul/li[3]').click()
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[4]/div[3]/div/input').send_keys('Passenger Test Three')
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[4]/div[4]/div/input').send_keys('3000000000')

    #infant1
    #titel
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[5]/div[2]/div/input').click()
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[5]/div[2]/div/div[3]/ul/li[1]').click()
    #inputname
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[5]/div[3]/div/input').send_keys('Baby One')
    #bday
    #DD
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[5]/div[4]/div/div[1]/div[1]/div/input').click()
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[5]/div[4]/div/div[1]/div[1]/div/div[3]/ul/li[3]').click()
    #MM
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[5]/div[4]/div/div[1]/div[3]/div/input').click()
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[5]/div[4]/div/div[1]/div[3]/div/div[3]/ul/li[1]').click()
    #YYYY
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[5]/div[4]/div/div[1]/div[5]/div/input').click()
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[5]/div[4]/div/div[1]/div[5]/div/div[3]/ul/li[1]').click()

    #infant2
    # titel
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[6]/div[2]/div/input').click()
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[6]/div[2]/div/div[3]/ul/li[2]').click()
    # inputname
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[6]/div[3]/div/input').send_keys('Baby Two')
    #bday
    #DD
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[6]/div[4]/div/div[1]/div[1]/div/input').click()
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[6]/div[4]/div/div[1]/div[1]/div/div[3]/ul/li[3]').click()
    #MM
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[6]/div[4]/div/div[1]/div[3]/div/input').click()
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[6]/div[4]/div/div[1]/div[3]/div/div[3]/ul/li[1]').click()
    #YYYY
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[6]/div[4]/div/div[1]/div[5]/div/input').click()
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[6]/div[4]/div/div[1]/div[5]/div/div[3]/ul/li[1]').click()

@when('Select Seats')
def seats(context):
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[4]/button[1]').click()
    time.sleep(5)
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div[4]/button').click()
    Confirm = context.driver.find_elements_by_xpath('//*[@id="popup"]/div/div/div/div[3]')
    if len(Confirm) == 1:
        context.driver.find_element_by_xpath('//*[@id="popup"]/div/div/div/div[5]/button[1]').click()
    else:
        pass

    time.sleep(10)

@when('Select Payment Method')
def payment(context):
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div[6]/div/a[1]/div').click()
    time.sleep(1)
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/label/div').click()
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/button').click()
    time.sleep(2)


@then('Verify payment')
def verifypage(context):
    #pop up salin nominal pembayaran
    status = context.driver.find_element_by_xpath('//*[@id="tooltip-container"]/div[2]').is_displayed()
    assert status is True

@then('Close Browser')
def closebrowser(context):
    context.driver.close()
