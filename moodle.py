from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chromedriver_path = '/Users/shreeyagokhale/miniconda3/lib/python3.11/site-packages/selenium/webdriver/chrome'
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://moovit.vit.ac.in/login/index.php")
driver.find_element(By.NAME, "username").send_keys("21BCE4009")
driver.find_element(By.NAME, "password").send_keys("191596@Abcd")
wait = WebDriverWait(driver, 10)
login_button = wait.until(EC.element_to_be_clickable((By.ID, "loginbtn")))
login_button.click()
wait = WebDriverWait(driver, 10)
main_page_element = (By.ID, "usernavigation")
wait.until(EC.presence_of_element_located(main_page_element))
print("Successfully navigated to the main page.")
time.sleep(3600)