from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

for i in range(20000, 30000):
    
    try:
        browser = webdriver.Chrome()
        wait = WebDriverWait(browser, 10)
        browser.get('https://captcha1.scrape.center/')
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.el-button')))
        button.click()
        geetest_slicebg = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.geetest_slicebg.geetest_absolute')))
        time.sleep(5)
        geetest_slicebg.screenshot(f'data/captcha/images/captcha_{i}.png')
    except Exception as e:
        print(e.args)
    finally:
        browser.close()
