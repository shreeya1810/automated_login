from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

message = input("Enter message")

driver.get("https://chat.openai.com/")
wait = WebDriverWait(driver, 15)
message_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='Send a message']")))
message_box.send_keys(message)
send_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Send']")))
send_button.click()
time.sleep(3600)