from selenium import webdriver
from shutil import which
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

def mint():

        drop_url = "https://magiceden.io/launchpad/sol_drunks"

        options = Options()
        chrome_path = "/Users/antonlysakov/tokens/chromedriver"
        options.add_extension("Phantom.crx")
#        options.add_argument("--disable-gpu")
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(executable_path=chrome_path, options=options)
        driver.get(drop_url)
        driver.maximize_window()
        txt = open("login.txt", 'r')
        read_txt = txt.readlines()
        values = []
        for x in read_txt:
                values.append(x)
        driver.switch_to.window(driver.window_handles[1])

        # button recovery phrase
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/main/div/div/section/button[2]")))
        recovery_phrase = driver.find_element(By.XPATH,"//*[@id='root']/main/div/div/section/button[2]").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Secret phrase']")))
        print("seed recovery")

        # seed import input and button click
        text_area = driver.find_element(By.XPATH,"//textarea[@placeholder='Secret phrase']").send_keys(values[0])
        import_btn = driver.find_element(By.XPATH,"//*[@id='root']/main/div[2]/div/form/div[2]/button").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/main/div[2]/div/div/button")))
        import_ = driver.find_element(By.XPATH,"//*[@id='root']/main/div[2]/div/div/button")
        driver.execute_script ("arguments[0].click();",import_)
        print("seed imported")

        # password set and confirm
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
        password1 = driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys(values[1])
        password2 = driver.find_element(By.XPATH,"//input[@placeholder='Confirm Password']").send_keys(values[1])
        check_box = driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
        submit = driver.find_element(By.XPATH,"//button[@type='submit']").click()
        print("password set")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Continue')]")))
        continue_btn = driver.find_element(By.XPATH,"//button[contains(text(),'Continue')]").click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Continue')]")))
        continue_btn_2 = driver.find_element(By.XPATH,"//button[contains(text(),'Continue')]").click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Finish')]")))
        finish_btn = driver.find_element(By.XPATH,"//button[contains(text(),'Finish')]").click()

        main_window = driver.window_handles[0]
        driver.switch_to.window(main_window)
        
        # extension setup done

        # now enabling phantom on this website

        select_wallet = driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div")
        select_wallet.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[1]/div/ul/li[1]/button")))
        phantom = driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/ul/li[1]/button")
        phantom.click()

        # TODO: might be worth to add this website to trusted app of this wallet

        original_window = driver.current_window_handle
        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(2))
        for window_handle in driver.window_handles:
                if window_handle != original_window:
                        driver.switch_to.window(window_handle)
                        break

        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Connect')]")))
        popup_connect = driver.find_element(By.XPATH,"//button[contains(text(),'Connect')]")
        popup_connect.click()
        print("fantom enabled waiting for mint")

      
        driver.switch_to.window(main_window)

        # Now setup is really finished and we ready to roll

        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Mint your token!')]")))
        mint_your_token = driver.find_element(By.XPATH,"//button[contains(text(), 'Mint your')]")
        driver.execute_script ("arguments[0].click();",mint_your_token)

        original_window = driver.current_window_handle
        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(2))
        for window_handle in driver.window_handles:
                if window_handle != original_window:
                        driver.switch_to.window(window_handle)
                        break


        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,"//button[contains(text(), 'Approve')]")))
        approve = driver.find_element(By.XPATH,"//button[contains(text(), 'Approve')]")
        #approve.click()
        print("Minting Finished")

mint()
