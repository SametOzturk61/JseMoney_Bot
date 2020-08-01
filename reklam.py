from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('JSEMONEY.XYZ LINK')

username = "USERNAME"
password = "PASSWORD"

usernameform = driver.find_element_by_xpath("/html/body/div/div[2]/form/table/tbody/tr[1]/td[2]/input")
usernameform.send_keys(username)

passwordform = driver.find_element_by_xpath("/html/body/div/div[2]/form/table/tbody/tr[3]/td[2]/input")
passwordform.send_keys(password)

driver.find_element_by_xpath("/html/body/div/div[2]/form/table/tbody/tr[5]/td/div/a").click()

sleep(2)

driver.get('JSEMONEY.XYZ LINK')

while True:
    numara1 = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/table/tbody/tr/td[1]/div/img").get_attribute("src")
    numara2 = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/table/tbody/tr/td[2]/div/img").get_attribute("src")
    numara3 = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/table/tbody/tr/td[3]/div/img").get_attribute("src")

    sayi = numara1[35:36] + numara2[35:36] + numara3[35:36]

    sayiform = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/input")
    sayiform.send_keys(sayi)

    driver.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/input").click()

print(sayi)
