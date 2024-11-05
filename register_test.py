import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("https://thinking-tester-contact-list.herokuapp.com/")

driver.find_element(By.ID, "signup").click()
driver.find_element(By.ID, "firstName").send_keys("Hello")
driver.find_element(By.ID, "lastName").send_keys("World")
driver.find_element(By.ID, "email").send_keys(f"helloworld123{random.randint(1, 9999999999)}@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("Helloworld123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(2)

logout_link = driver.find_element(By.XPATH, "//button[text()='Logout']")
logout_link.click()

time.sleep(2)

email_field = driver.find_element(By.ID, "email")
if email_field.is_displayed():
    print("Logout successful! The user has been redirected to the login page.")
else:
    print("We couldn't find the specific login page elements. Check again.")

driver.quit()


