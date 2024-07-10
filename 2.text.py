from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



# Create a new instance of the web driver

driver = webdriver.Firefox()

try:
    # Open the website
    driver.get("https://www.saucedemo.com/")

    # Find the username and password input fields
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")

    # Enter the credentials
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Wait for a few seconds to ensure the page loads
    time.sleep(3)

    # Extract the entire contents of the page
    page_source = driver.page_source

    # Save the contents to a text file
    with open("Webpage_task_11.txt", "w", encoding='utf-8') as file:
        file.write(page_source)

    # Print confirmation
    print("Page contents have been saved to Webpage_task_11.txt")

finally:
    # Close the browser
    driver.quit()
