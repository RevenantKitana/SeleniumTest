from selenium import webdriver
from selenium.webdriver.edge.service import Service
import os
import sys

def setup_browser():
    # Corrected WebDriver path and filename
    driver_path = r"E:\CNPM\Test&\SeleniumTest\msedgedriver.exe"
    
    # Verify if WebDriver exists
    if not os.path.isfile(driver_path):
        error_msg = f"WebDriver not found at {driver_path}. Please ensure msedgedriver.exe is placed in E:\\CNPM\\Test&."
        print(error_msg, file=sys.stderr)
        raise FileNotFoundError(error_msg)
    
    service = Service(driver_path)
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    try:
        driver = webdriver.Edge(service=service, options=options)
        driver.get("https://www.advantageonlineshopping.com/")
        return driver
    except Exception as e:
        error_msg = f"Failed to initialize Edge WebDriver: {str(e)}"
        print(error_msg, file=sys.stderr)
        raise

def close_browser(driver):
    if driver:
        try:
            driver.quit()
        except Exception as e:
            print(f"Error closing browser: {str(e)}", file=sys.stderr)