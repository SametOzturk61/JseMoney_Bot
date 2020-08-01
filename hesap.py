from time import sleep
from selenium import webdriver
import random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

referrallink = "REFERRAL LINK"

while True:
   driver = webdriver.Chrome()

   driver.get(referrallink)

   driver.find_element_by_xpath("/html/body/div/div[1]/div/ul/li[3]/a").click()

   username = randomword(15)
   email = randomword(10) + "@gmail.com"
   password = randomword(15)

   usernameform = driver.find_element_by_xpath("/html/body/div/div[2]/form/table/tbody/tr[1]/td[2]/input")
   usernameform.send_keys(username)

   emailform = driver.find_element_by_xpath("/html/body/div/div[2]/form/table/tbody/tr[3]/td[2]/input")
   emailform.send_keys(email)

   passwordform = driver.find_element_by_xpath("/html/body/div/div[2]/form/table/tbody/tr[5]/td[2]/input")
   passwordform.send_keys(password)

   passwordform2 = driver.find_element_by_xpath("/html/body/div/div[2]/form/table/tbody/tr[7]/td[2]/input")
   passwordform2.send_keys(password)

   sleep(3)

   driver.find_element_by_xpath("/html/body/div/div[2]/form/table/tbody/tr[12]/td/div/a").click()

   sleep(2)

   driver.get("https://jsemoney.xyz/logout.php")
   driver.close()

