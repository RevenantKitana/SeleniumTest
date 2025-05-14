from selenium.webdriver.common.by import By
import time
from utils.file_handler import load_random_account

def is_logged_in(driver):
    try:
        driver.find_element(By.XPATH, "//span[@class='hi-user containMiniTitle ng-binding']")
        return True
    except:
        return False

def click_sign_out(driver):
    try:
        driver.find_element(By.ID, "menuUserLink").click()
        time.sleep(1)
        sign_out_btn = driver.find_element(By.XPATH, "//label[@translate='Sign_out']")
        driver.execute_script("arguments[0].click();", sign_out_btn)
        time.sleep(2)
        print("Sign out: SUCCESS")
        return True
    except Exception as e:
        print(f"Sign out: FAILED - {e}")
        return False

def login_logout(driver, username=None, password=None, remember_me=False):
    try:
        # Nếu đã đăng nhập thì đăng xuất trước
        if is_logged_in(driver):
            print("Already logged in. Logging out first...")
            time.sleep(1)
            click_sign_out(driver)
            time.sleep(1)

        # Đóng popup nếu đang mở
        try:
            driver.find_element(By.CLASS_NAME, "closeBtn").click()
            time.sleep(1)
        except:
            pass

        # Mở popup đăng nhập
        driver.find_element(By.ID, "menuUserLink").click()
        time.sleep(1)

        if username and password:
            # Nhập thông tin đăng nhập
            time.sleep(1)
            driver.find_element(By.NAME, "username").clear()
            time.sleep(1)
            driver.find_element(By.NAME, "username").send_keys(username)
            time.sleep(1)
            driver.find_element(By.NAME, "password").clear()
            time.sleep(1)
            driver.find_element(By.NAME, "password").send_keys(password)

            # Chọn/bỏ chọn checkbox Remember Me
            checkbox = driver.find_element(By.NAME, "remember_me")
            if remember_me:
                while not checkbox.is_selected():
                    checkbox.click()
                    time.sleep(0.2)
            else:
                while checkbox.is_selected():
                    checkbox.click()
                    time.sleep(0.2)

            driver.find_element(By.ID, "sign_in_btn").click()
            time.sleep(3)

            # Kiểm tra tên người dùng hiển thị
            driver.find_element(By.XPATH, f"//span[contains(text(), '{username}')]")
            print("Login verification: SUCCESS")

            # Load lại trang và kiểm tra session
            driver.get("about:blank")
            time.sleep(2)
            driver.get("https://www.advantageonlineshopping.com/")
            time.sleep(9)

            if remember_me:
                # Kiểm tra có còn đăng nhập sau reload
                driver.find_element(By.XPATH, f"//span[contains(text(), '{username}')]")
                print("Session persistence: VERIFIED")
                time.sleep(1)
                click_sign_out(driver)
                print("Post-login logout: SUCCESS")
            else:
                # Kiểm tra đã bị đăng xuất sau reload
                try:
                    driver.find_element(By.XPATH, f"//span[contains(text(), '{username}')]")
                    time.sleep(1)
                    print("Session persistence (expected logout): FAILED")
                    time.sleep(1)
                    click_sign_out(driver)
                    return False
                except:
                    print("Session persistence (expected logout): VERIFIED")

            return True

        else:
            # Đăng nhập sai
            driver.find_element(By.NAME, "username").clear()
            driver.find_element(By.NAME, "username").send_keys("wronguser")
            driver.find_element(By.NAME, "password").clear()
            driver.find_element(By.NAME, "password").send_keys("wrongpass")
            driver.find_element(By.ID, "sign_in_btn").click()
            time.sleep(2)

            error_label = driver.find_element(By.XPATH, "//label[text()='Incorrect user name or password.']")
            if error_label.is_displayed():
                print("Invalid login error detected: SUCCESS")
                return True
            else:
                print("Invalid login error NOT found")
                return False

    except Exception as e:
        print(f"Login/Logout failed: {e}")
        return False


def test_login(driver):
    try:
        account = load_random_account()
        if not account:
            print("Login Test: SKIPPED - No accounts available")
            return

        print(f"Account loaded: {account['username']}")
        print("Starting Login Test")

        # Test login với Remember Me
        if login_logout(driver, account["username"], account["password"], remember_me=True):
            print("Valid Login with Remember Me Test: SUCCESS")
        else:
            print("Valid Login with Remember Me Test: FAILED")

        # Test login không Remember Me
        if login_logout(driver, account["username"], account["password"], remember_me=False):
            print("Valid Login without Remember Me Test: SUCCESS")
        else:
            print("Valid Login without Remember Me Test: FAILED")

        # Test đăng nhập sai
        if login_logout(driver):
            print("Invalid Login Test: SUCCESS")
        else:
            print("Invalid Login Test: FAILED")

    except Exception as e:
        print(f"Login Test: FAILED - {e}")

def login_only(driver):
    if is_logged_in(driver):
        time.sleep(2)
        print("Already logged in.")
    else:
        try:
            driver.find_element(By.ID, "menuUserLink").click()
            time.sleep(1)
            account = load_random_account()
            if not account:
                print("Login Test: SKIPPED - No accounts available")
                return
            print(f"Account loaded: {account['username']}")
            print("Starting Login Test")
            # Nhập thông tin đăng nhập
            driver.find_element(By.NAME, "username").clear()
            driver.find_element(By.NAME, "username").send_keys(account["username"])
            driver.find_element(By.NAME, "password").clear()
            driver.find_element(By.NAME, "password").send_keys(account["password"])
            driver.find_element(By.ID, "sign_in_btn").click()
            time.sleep(3)
        except Exception as e:
            print(f"Login Test: FAILED - {e}")