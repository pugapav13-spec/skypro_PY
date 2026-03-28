from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.get("http://uitestingplayground.com/dynamicid")
time.sleep(2)

button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

button.click()
print("Синяя кнопка нажата")

time.sleep(2)
driver.quit()
