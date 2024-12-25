import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up logging
logging.basicConfig(level=logging.INFO)

# Setup Selenium WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#logging.info(len(dropdown1.options))
def search(first_name, last_name,):
    try:
        # Input the first and last name
        driver.find_element(By.NAME, "firstName").clear()
        driver.find_element(By.NAME, "firstName").send_keys(first_name)
        driver.find_element(By.NAME, "lastName").clear()
        driver.find_element(By.NAME, "lastName").send_keys(last_name)
        logging.info(f"Entered first name: {first_name} and last name: {last_name}.")

        # Click the search button
        driver.find_element(By.NAME, "submitLink").click()
        logging.info("Clicked the search button.")
        
        # Optionally, wait for search results and take a screenshot
        #time.sleep(1)  # Adjust as necessary for the search results to load
        screenshot_path = f"screenshot_{court_department_name}_{j}_{k}.png"
        driver.save_screenshot(screenshot_path)
        logging.info(f"Screenshot saved to {screenshot_path}.")

        # Go back to the form page to perform the next iteration
        driver.back()
        logging.info("Navigated back to the form page.")
        #time.sleep(5)  # Wait for the form page to load again

    except Exception as e:
        logging.error(f"An error occurred: {e}")

    finally:
        # Close the browser
        logging.info("Closing the browser...")
        driver.quit()
