import csv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

driver = webdriver.Chrome()
driver.get('https://www.realauction.com/clients')

# Wait for the page to load
wait = WebDriverWait(driver, 10)
client_list = wait.until(EC.presence_of_element_located((By.ID, 'clientList')))

all_links = []

# Iterate over the buttons
for i in range(2, 7):
    try:
        if( i != 2 ):
            button_xpath = f'/html/body/div[5]/div/div[4]/div[2]/div[2]/button[{i}]'
            button = wait.until(EC.presence_of_element_located((By.XPATH, button_xpath)))
            button.click()
            sleep(1)
        all_elements = []
        all_elements = driver.find_elements(By.CLASS_NAME, 'client-box')
        for j in range(0, len(all_elements)):
            sheet.append([all_elements[j].get_attribute("data-client-link")])
        sleep(1)
    except Exception as e:
        print(f"Error occurred: {e}")
sleep(2)

workbook.save(os.path.normpath("./" + "URLs.xlsx"))


# with open('URLs.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(all_links)