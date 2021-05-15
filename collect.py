from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time
from loguru import logger

COUNT = 1000

for i in range(0, COUNT + 1):
    try:
        browser = webdriver.Chrome()
        wait = WebDriverWait(browser, 10)
        browser.get('https://captcha1.scrape.center/')
        button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.el-button')))
        button.click()
        captcha = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.geetest_slicebg.geetest_absolute')))
        time.sleep(5)
        captcha.screenshot(f'data/captcha/images/captcha_{i}.png')
    except WebDriverException as e:
        logger.error(f'webdriver error occurred {e.msg}')
    finally:
        browser.close()
