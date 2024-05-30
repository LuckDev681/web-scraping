from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
from selenium.common.exceptions import NoSuchElementException
import csv

driver = webdriver.Chrome()
URL = 'https://broward.realforeclose.com/'
driver.get(URL)

username=driver.find_element(By.XPATH, '//*[@id="LogName"]')
username.send_keys("321")
password=driver.find_element(By.XPATH, '//*[@id="LogPass"]')
password.send_keys("1234567")
driver.find_element(By.XPATH, '//*[@id="LogButton"]').click()
time.sleep(3)
while True:
    try:
        try:
            driver.find_element(By.XPATH, '//*[@id="BNOTACC"]').click()
        except NoSuchElementException:
            driver.find_element(By.XPATH, '//*[@id="BNOTOK"]').click()
        time.sleep(5)
    except:
        try:
            request=driver.find_element(By.XPATH, '//*[@id="ln_menu"]/div[4]/a/span')
            driver.find_element(By.XPATH, '//*[@id="ln_menu"]/div[10]/a/span').click()
            break
        except NoSuchElementException:
            driver.find_element(By.XPATH, '//*[@id="ln_menu"]/div[9]/a').click()
            break
time.sleep(10)

try:
    driver.find_element(By.XPATH, '//*[@id="FilterBox"]/div[7]/button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="FilterBox"]/div[7]/div/ul/li[3]/label').click()
    driver.find_element(By.XPATH, '//*[@id="FilterBox"]/div[7]/div/ul/li[4]/label').click()
except NoSuchElementException:
    driver.find_element(By.XPATH, '//*[@id="AUCT_TYPE"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="AUCT_TYPE"]/option[2]').click()
    
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="testBut"]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="t_main_report"]/a[1]/img').click()
csv_file_path=r'C:\Users\Administrator\Downloads\QuickSearch.csv'
time.sleep(1)
new_column1_header = 'Property Owner'
data_with_new_column = []
with open(csv_file_path, 'r', newline='') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)  # Read the existing headers
    headers.append(new_column1_header)  # Add the new column header
    data_with_new_column.append(headers)  # Append the updated headers
    for row in csv_reader:
        row.append('')  # Add an empty value for the new column in each row
        data_with_new_column.append(row)

# Write the updated data with the new column back to the CSV file
with open(csv_file_path, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data_with_new_column)

new_column2_header = 'Mailing Address'
data_with_new_column = []
with open(csv_file_path, 'r', newline='') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)  # Read the existing headers
    headers.append(new_column2_header)  # Add the new column header
    data_with_new_column.append(headers)  # Append the updated headers
    for row in csv_reader:
        row.append('')  # Add an empty value for the new column in each row
        data_with_new_column.append(row)

# Write the updated data with the new column back to the CSV file
with open(csv_file_path, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data_with_new_column)
csv_file_path=r'C:\Users\Administrator\Downloads\QuickSearch.csv'
row_count = 0
# Open the CSV file and count the rows
with open(csv_file_path, 'r') as file:
    for row in file:
        row_count += 1
real = row_count-5
count = real/30
rest = real%30
for j in range(0,count-1):
    for i in range(2,31):
        addxpath=f'/html/body/table/tbody/tr/td[2]/div[2]/div/div/div[3]/div[4]/div/table/tbody/tr[{i}]/td[11]'
        addtext=driver.find_element(By.XPATH, addxpath).text
        if addtext !=" ":
            xpath = f'/html/body/table/tbody/tr/td[2]/div[2]/div/div/div[3]/div[4]/div/table/tbody/tr[{i}]/td[3]/a'
            driver.find_element(By.XPATH, xpath).click()        
            time.sleep(5)
            windows = driver.window_handles
            driver.switch_to.window(windows[1])
            time.sleep(3)
            driver.find_element(By.CSS_SELECTOR, '#FRM_ADetails > tbody > tr:nth-child(2) > td.FMM.FSMM17 > div.bRowA > a:nth-child(1)').click()
            time.sleep(2)

            pyautogui.press('enter')
            
            time.sleep(3)
            windows = driver.window_handles
            driver.switch_to.window(windows[2])
            time.sleep(2)
            Owner = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/table/tbody/tr[1]/td[1]/table[1]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/span').text
            mailing = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/table/tbody/tr[1]/td[1]/table[1]/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/span').text
            
            data_with_new_data = []
            with open(csv_file_path, 'r', newline='') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    data_with_new_data.append(row)
            data_with_new_data[i-1][15] = Owner
            data_with_new_data[i-1][16] = mailing
            with open(csv_file_path, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(data_with_new_data)

            driver.close()
            driver.switch_to.window(windows[1])
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="next_pager"]/span').click()
for i in range(2,rest):
        addxpath=f'/html/body/table/tbody/tr/td[2]/div[2]/div/div/div[3]/div[4]/div/table/tbody/tr[{rest}]/td[11]'
        addtext=driver.find_element(By.XPATH, addxpath).text
        if addtext !=" ":
            xpath = f'/html/body/table/tbody/tr/td[2]/div[2]/div/div/div[3]/div[4]/div/table/tbody/tr[{rest}]/td[3]/a'
            driver.find_element(By.XPATH, xpath).click()        
            time.sleep(5)
            windows = driver.window_handles
            driver.switch_to.window(windows[2])
            time.sleep(3)
            driver.find_element(By.CSS_SELECTOR, '#FRM_ADetails > tbody > tr:nth-child(2) > td.FMM.FSMM17 > div.bRowA > a:nth-child(1)').click()
            time.sleep(2)

            pyautogui.press('enter')
            
            time.sleep(3)
            windows = driver.window_handles
            driver.switch_to.window(windows[3])
            time.sleep(2)
            Owner = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/table/tbody/tr[1]/td[1]/table[1]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/span').text
            mailing = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/table/tbody/tr[1]/td[1]/table[1]/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/span').text
            
            data_with_new_data = []
            with open(csv_file_path, 'r', newline='') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    data_with_new_data.append(row)
            data_with_new_data[i-1][15] = Owner
            data_with_new_data[i-1][16] = mailing
            with open(csv_file_path, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(data_with_new_data)

            driver.close()
            driver.switch_to.window(windows[1])
            time.sleep(3)
time.sleep(50)

driver.quit()