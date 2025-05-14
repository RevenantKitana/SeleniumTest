import sys
import os
import time
from tests import test_login
from utils.logger import setup_logger
from utils.browser import setup_browser, close_browser
from tests.test_register import test_register
from tests.test_login import test_login,login_only

def main():
    logger = setup_logger()
    driver = setup_browser()
    print("Wait for homepage to load...")
    time.sleep(3)
    while True:
        print("\n=== Advantage Online Shopping Test Menu ===")
        print("1. Test Register")
        print("2. Test Login - Logout")
        print("3. Login only")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        logger.info(f"User selected option: {choice}")
        
        try:
            if choice == "1":
                test_register(driver, logger)
            elif choice == "2":
                test_login(driver)
            elif choice == "3":
                login_only(driver)
            elif choice == "4":
                logger.info("Exiting program")
                break
            else:
                print("Invalid choice. Please select 1-4.")
                logger.warning(f"Invalid choice entered: {choice}")
        except Exception as e:
            print(f"Error during test execution: {str(e)}")
            logger.error(f"Test execution error: {str(e)}")
    
    close_browser(driver)
    print("Browser closed. Program terminated.")

if __name__ == "__main__":
    main()