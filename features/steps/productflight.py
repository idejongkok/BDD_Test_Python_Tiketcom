from behave import *
from selenium import webdriver
import time


@given('Relaunch Chrome browser')
def openbrowser(context):
    context.driver  = webdriver.Chrome('C:\driver\chromedriver\chromedriver.exe')


@when('Open homepage')
def openhomepage(context):
    context.driver.get('https://www.tiket.com/')
    context.driver.implicitly_wait(10)

    Blocker = context.driver.find_elements_by_xpath('//*[@id="ab-iam-0852068100e25b53bf268f196f732e8a"]/div[2]/button')
    if len(Blocker) == 1:
        context.driver.find_element_by_xpath('//*[@id="ab-iam-0852068100e25b53bf268f196f732e8a"]/div[2]/button').click()
    else:
        pass
    context.driver.implicitly_wait(5)

@when('Login with email')
def loginemail(context):
    context.driver.find_element_by_link_text('Login').click()
    context.driver.implicitly_wait(5)
    time.sleep(3)
    context.driver.find_element_by_name('username').send_keys('swtester.uno@gmail.com') #change send_keys value to your registeres email
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/div/div[3]/div[2]/div/div/div/div/div[1]/div[4]').click()
    context.driver.implicitly_wait(5)
    time.sleep(2)
    context.driver.find_element_by_name('password').send_keys('asdfQWER12#$') #change send_keys value to your password
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div[2]/div/form/div[4]').click()
    #wait for OTP Code which should be sent your mobile phone number . You must input manually the OTP code to the input form. You have 20 secs to do that.
    time.sleep(20)


@when('Select "Pesawat" Menu')
def selectmenu(context):
    context.driver.find_element_by_link_text('Pesawat').click()
    context.driver.implicitly_wait(5)
    time.sleep(3)

@when('Select "Pulang-pergi" Option')
def selecttype(context):
    context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[2]/div/div[2]').click()
    time.sleep(1)

@when('Select Origin Point')
def originpoint(context):
    context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]').click()
    context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div/ul/li[2]/div/div').click()
    time.sleep(1)

@when('Select Destination Point')
def destinationpoint(context):
    context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/input').send_keys('Denpasar')
    context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div/ul/div/div/div/li/div/div').click()
    time.sleep(1)

@when('Select Departure date')
def departuredate(context):
    context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[3]/div[4]/div[2]/div[2]/div/input').click()
    context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[3]/div[4]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td[7]/div').click()
    time.sleep(1)

@when('Select Comeback date')
def comebackdate(context):
    context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[3]/div[5]/div[2]/div[2]/div/input').click()
    context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[3]/div[5]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/table/tbody/tr[4]/td[2]/div').click()
    time.sleep(1)


@when('Select Pax & Class')
def paxclass(context):
    context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[3]/div[6]/div[2]/div/input').click()
    context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[3]/div[6]/div[2]/div/div/div[3]/button').click()
    time.sleep(1)

@when('Search Route')
def searchroute(context):
    context.driver.find_element_by_xpath('//*[@id="formhome"]/div/div/div[1]/div[4]/button').click()
    #context.driver.implicitly_wait(5)
    time.sleep(5)

@when('Select flight')
def selectflight(context):
    Information = context.driver.find_elements_by_xpath('//*[@id="app"]/div/div[5]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]')
    if len(Information) == 1:
        context.driver.find_element_by_xpath('//*[@id="app"]/div/div[5]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]').click()
    else:
        pass
    time.sleep(5)
    #transit
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[2]/div/div[2]/div/div[1]/div/form/div/div[1]/div/div[2]/div/div[4]/div/label').click()
    time.sleep(1)
    #depttime
    # context.driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[2]/div/div[2]/div/div[1]/div/form/div/div[3]/div/div[2]/div/div[2]/div[3]/div/label').click()
    # time.sleep(1)
    #selectroute
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div[1]/div').click()

    # context.driver.implicitly_wait(5)
    time.sleep(5)

@when('Select flight home')
def selectflighthome(context):
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[2]/div/div[2]/div/div[1]/div/form/div/div[1]/div/div[2]/div/div[3]/div').click()
    time.sleep(1)
    # context.driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[2]/div/div[2]/div/div[1]/div/form/div/div[3]/div/div[2]/div/div[2]/div[4]/div').click()
    # time.sleep(1)
    # context.driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[2]/div/div[2]/div/div[1]/div/form/div/div[4]/div/div[2]/div/div[5]/div[2]').click()
    # time.sleep(1)
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div[1]').click()
    time.sleep(1)
    #context.driver.implicitly_wait(5)
    time.sleep(10)


@when('Go to Pax Detail Page')
def selectflighthome(context):
    BLocker2 = context.driver.find_elements_by_xpath('//*[@id="ab-iam-62ca5cc070b04f5eca3d510e6044349e"]/div[1]')
    if len(BLocker2) == 1:
        context.driver.find_element_by_xpath('//*[@id="ab-iam-62ca5cc070b04f5eca3d510e6044349e"]/div[2]/div[2]/button[2]').click()
    else:
        pass
    time.sleep(3)

@when('Input Pax Info')
def inputpaxinfo(context):
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[1]/label/span[2]').click()
    time.sleep(1)
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div/input').click()
    time.sleep(1)
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div/div[3]/div[2]/ul/li[1]').click()
    time.sleep(1)
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[3]/div/div[2]/div/div[1]/div/div[6]/button').click()
    time.sleep(1)
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[3]/div/div[3]/div/div/div/div/div[3]/button[2]').click()
    time.sleep(5)

@when('Select Payment Method with Virtual Account')
def inputpaymentmethod(context):
    #Select BCA Virtual Account
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/a[1]/div/div').click()
    time.sleep(4)
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/label/div').click()
    time.sleep(1)
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/button').click()
    time.sleep(5)

@then('Complete the order')
def complete(context):
    check = context.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/div/p').is_displayed()
    assert check is True

@then('Logout')
def logout(context):
    context.driver.get('https://www.tiket.com/')
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/div[1]/div[3]/div/div[2]/div/span').click()
    context.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/div[1]/div[4]/div/div[2]/div/div/div[2]/div').click()
    context.driver.find_element_by_xpath('//*[@id="modal-root"]/div/div/div/div/div[4]/div[1]').click
    time.sleep(5)

@then('Close the Browser')
def Close(context):
    context.driver.close()


