from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://vtop.vit.ac.in/vtop")

initial_button = driver.find_element(By.CSS_SELECTOR, "div.cardStudent button")
initial_button.click()
driver.find_element(By.NAME, "username").send_keys("SHREEYA1810")
driver.find_element(By.NAME, "password").send_keys("Aariah@0818")
wait = WebDriverWait(driver, 10)
login_button = wait.until(EC.element_to_be_clickable((By.ID, "submitBtn")))
login_button.click()
main_page_element = (By.ID, "myModalFooter")
wait.until(EC.presence_of_element_located(main_page_element))
print("Successfully navigated to the main page.")
time.sleep(3600)