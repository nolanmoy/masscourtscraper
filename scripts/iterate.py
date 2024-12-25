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
def court_department_iterate(court_department_name, first_name, last_name):
    try:
        # Open the webpage
        logging.info("Opening the webpage...")
        driver.get("https://www.masscourts.org/eservices/home.page.2")

        # Wait for user to solve the CAPTCHA manually if needed
        logging.info("Please solve the CAPTCHA manually in the browser window if present.")
        time.sleep(15)  # Wait for 60 seconds (adjust as needed)

        # Define the first and last name to be used for each search
        dropdown1 = Select(WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.NAME, "sdeptCd"))))
        # Iterate through all options in the first dropdown
        dropdown1.select_by_visible_text(court_department_name)
                
                
        #logging.info(f"Selected option {dropdown1.options[court_departme].text} in dropdown1.")
        dropdown2 = Select(WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.NAME, "sdivCd"))))

        #time.sleep(2)  # Wait for the second dropdown to be populated

        # Iterate through all options in the second dropdown
        for j in range(len(dropdown2.options)-1):
            if j == 0:
                dropdown2.select_by_index(j+1)
                dropdown2 = Select(WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.NAME, "sdivCd"))))
            else:
                dropdown2 = Select(WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.NAME, "sdivCd"))))
                dropdown2.select_by_index(j)
            
            logging.info(f"Selected option {dropdown2.options[j].text} in dropdown2.")
            #time.sleep(2)  # Wait for the third dropdown to be populated
            dropdown3 = Select(WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.NAME, "slocCd"))))

            # Iterate through all options in the third dropdown
            for k in range(len(dropdown3.options)):
                dropdown3.select_by_index(k)
                logging.info(f"Selected option {dropdown3.options[k].text} in dropdown3.")
                time.sleep(2)  # Wait for any dynamic content to load

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

court_department_iterate("District Court", "John", "Doe")
