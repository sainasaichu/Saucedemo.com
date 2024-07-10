from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to your WebDriver executable'

# Create a new instance of the web driver
driver = webdriver.Firefox

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

    # Fetch the title of the page
    title = driver.title

    # Print the title
    print(f"Page Title: {title}")

finally:
    # Close the browser
    driver.quit()
