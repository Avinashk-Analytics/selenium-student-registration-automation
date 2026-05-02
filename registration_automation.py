#Import Required Selenium Dependencies

from selenium import webdriver
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

# Setup Browser
driver = webdriver.Chrome()
driver.get("https://demoqa.com/")
driver.maximize_window()
driver.implicitly_wait(5)

#Click on element
driver.find_element(By.XPATH,"//div[@class= 'card-up']").click()

#Handle Scrollbar
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

#click on forms
driver.find_element(By.XPATH, "//div[text()='Forms']").click()

#Click on Practice forms
driver.find_element(By.XPATH,"//a[@href='/automation-practice-form']").click()
time.sleep(2)

#---------------------------Locate Each field on registration form-----------------------------------------

driver.find_element(By.ID,"firstName").send_keys("Avinash")
driver.find_element(By.ID,"lastName").send_keys("Kadhare")
driver.find_element(By.ID,"userEmail").send_keys("avi124@email.com")

genders= driver.find_elements(By.XPATH,"//input[@name='gender']")
for gender in genders:
    if gender.get_attribute("value") == "Male":
        gender.click()
        gender.is_selected()
        break

driver.find_element(By.ID,"userNumber").send_keys("7506922132")

wait = WebDriverWait(driver, 10)

# 1. Wait for the date input to be clickable
date_input = wait.until(EC.element_to_be_clickable((By.ID, "dateOfBirthInput")))

#2. Open the calendar
date_input.click()

# 3. Select Month
month_dropdown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__month-select")))
Select(month_dropdown).select_by_value("7")  # August = 7 (0-based)

# 4. Select Year
year_dropdown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__year-select")))
Select(year_dropdown).select_by_value("1995")

# 5. Select Day
day = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='11' and not(contains(@class,'outside-month'))]")))
day.click()

# 6. Trigger update in input (press TAB)
date_input.send_keys(Keys.TAB)


driver.find_element(By.XPATH, "//input[contains(@class,'subjects-auto-complete__input')]").send_keys("All")

Hobbies = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for hobbies in Hobbies:
    if hobbies.get_attribute("value") == "2":
        hobbies.click()
        hobbies.is_selected()
        break

upload = driver.find_element(By.ID, "uploadPicture").send_keys("C:\\Users\\AK47\\Pictures\\group_1.PNG")

driver.find_element(By.ID,"currentAddress").send_keys("abc123,city")

# Select State
state_dropdown = driver.find_element(By.ID, "state")

state_input = driver.find_element(By.XPATH, "//div[@id='state']//input")
state_input.send_keys("Uttar Pradesh")
state_input.send_keys(Keys.ENTER)

time.sleep(2)

# Select City
city_dropdown = driver.find_element(By.ID, "city")

city_input = driver.find_element(By.XPATH, "//div[@id='city']//input")
city_input.send_keys("Lucknow")
city_input.send_keys(Keys.ENTER)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

driver.find_element(By.CSS_SELECTOR,".btn.btn-primary").click()
confirm_message = driver.find_element(By.XPATH, "//div[@id='example-modal-sizes-title-lg']").text
assert "Thanks for submitting the form" in confirm_message

driver.find_element(By.ID, "closeLargeModal").click()

time.sleep(5)
driver.quit()