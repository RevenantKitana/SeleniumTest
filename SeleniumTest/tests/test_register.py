from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.data_generator import generate_user_data
from utils.file_handler import save_account
from type_data import typedata
import time

def test_register(driver, logger):
    print ("Starting Register Test")
    try:
        # Navigate to registration page
        driver.find_element(By.ID, "menuUser").click()
        time.sleep(2)  # Wait for user menu to open
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "CREATE NEW ACCOUNT"))).click()
        time.sleep(2)  # Wait for registration page to load
        
        # Valid registration
        print("Creating data...")
        user_data = generate_user_data()
        print(user_data)
        print("Insert data...")
        typedata(driver.find_element(By.NAME, "usernameRegisterPage"), user_data["username"])
        typedata(driver.find_element(By.NAME, "emailRegisterPage"), user_data["email"])
        typedata(driver.find_element(By.NAME, "passwordRegisterPage"), user_data["password"])
        typedata(driver.find_element(By.NAME, "confirm_passwordRegisterPage"), user_data["password"])
        typedata(driver.find_element(By.NAME, "first_nameRegisterPage"), user_data["first_name"])
        typedata(driver.find_element(By.NAME, "last_nameRegisterPage"), user_data["last_name"])
        typedata(driver.find_element(By.NAME, "phone_numberRegisterPage"), user_data["phone"])
        typedata(driver.find_element(By.NAME, "countryListboxRegisterPage"), user_data["country"])
        typedata(driver.find_element(By.NAME, "cityRegisterPage"), user_data["city"])
        typedata(driver.find_element(By.NAME, "addressRegisterPage"), user_data["address"])
        typedata(driver.find_element(By.NAME, "state_/_province_/_regionRegisterPage"), user_data["state"])
        typedata(driver.find_element(By.NAME, "postal_codeRegisterPage"), user_data["postcode"])

        time.sleep(1)
        driver.find_element(By.NAME, "i_agree").click()
        time.sleep(1)
        driver.find_element(By.ID, "register_btn").click()
        time.sleep(2)
        
        # Verify registration success
        WebDriverWait(driver, 10).until(EC.url_contains("https://www.advantageonlineshopping.com/#/"))
        print("Registration successful")
        save_account(user_data)
        logger.info("Account saved")
        print("Registration Test: SUCCESS! Account "+ user_data["username"]+ " has been registered!")
        time.sleep(5)  # Wait
        print("Try to register with username " + user_data["username"])
        driver.get("https://www.advantageonlineshopping.com/")
        time.sleep(5)  # Wait for homepage to load
        driver.find_element(By.ID, "menuUser").click()
        time.sleep(3)  # Wait for user menu to open
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "CREATE NEW ACCOUNT"))).click()
        time.sleep(3)  # Wait for registration page to load
        typedata(driver.find_element(By.NAME, "usernameRegisterPage"), user_data["username"])
        typedata(driver.find_element(By.NAME, "emailRegisterPage"), "test@test.com")
        typedata(driver.find_element(By.NAME, "passwordRegisterPage"), "A1b2c")
        typedata(driver.find_element(By.NAME, "confirm_passwordRegisterPage"), "A1b2c")
        typedata(driver.find_element(By.NAME, "first_nameRegisterPage"), "Johnny")
        typedata(driver.find_element(By.NAME, "last_nameRegisterPage"), "Cage")
        typedata(driver.find_element(By.NAME, "phone_numberRegisterPage"), "0987654321")
        typedata(driver.find_element(By.NAME, "countryListboxRegisterPage"), "VietNam")
        typedata(driver.find_element(By.NAME, "cityRegisterPage"), "TheCity")
        typedata(driver.find_element(By.NAME, "addressRegisterPage"), "Address")
        typedata(driver.find_element(By.NAME, "state_/_province_/_regionRegisterPage"), "state")
        typedata(driver.find_element(By.NAME, "postal_codeRegisterPage"), "12345")
        time.sleep(1)  # Wait after entering confirm password
        time.sleep(1)
        driver.find_element(By.NAME, "i_agree").click()
        time.sleep(1)
        driver.find_element(By.ID, "register_btn").click()
        time.sleep(2)
        # Check for specific error message
        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'User name already exists')]"))
        )
        if error:
            logger.info("Invalid registration detected with message: 'User name already exists'")
            print("User name already exists! Invalid Registration Test: SUCCESS")
        else:
            logger.error("Expected 'User name already exists' message not found")
            print("Invalid Registration Test: FAILED")
            
    except Exception as e:
        logger.error(f"Register Test failed: {str(e)}")
        print(f"Register Test: FAILED - {str(e)}")