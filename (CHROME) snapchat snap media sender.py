import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('debuggerAddress', 'localhost:9222')
driver = webdriver.Chrome(options=chrome_options)


loop_count = 0

# open this in file manager address bar
# "C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir=D:\chromeData"

while True:
    try:
        loop_count = loop_count + 1
        open_camera_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cDumY"))
        )
        open_camera_button.click()
        capture_camera_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".FBYjn"))
        )
        capture_camera_button.click()
        send_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".TYX6O"))
        )
        send_button.click()
        # message_input_div = WebDriverWait(driver, 3).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "euyIb"))
        # )
        # message_input_div.click()
        # message_input_div.send_keys(Keys.CONTROL+"v")
        # message_input_div.send_keys(Keys.ENTER)
        print('snap sent : ', loop_count)
        # time.sleep(1.5)

    except Exception as e:
        print('An Error Occured...')
