from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions
# We don't want to open the webpage in a real browser, but in a headless browser.
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

auth_data = {"login": "P2536017137_3981-operator", "password": "995F703B6E5550970B70E200E28039B3", "language": "ru"}

driver.get("https://securepayments.sberbank.ru/mportal3/admin")
try:
    element = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="login"]'))
    )
    login_input = driver.find_element(By.XPATH, '//*[@id="login"]')
    login_input.send_keys(auth_data['login'])

    password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_input.send_keys(auth_data['password'])

    submit_btn = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[1]/div/div[1]/div/div[2]/form/button')
    submit_btn.click()

    sleep(3)
    js_script = '''
    document.getElementsByClassName('modal-window-container').forEach(ele => ele.style.display = "none")
     '''
    driver.execute_script(js_script)

    transaction_btn = driver.find_element(By.XPATH,
                                          '/html/body/div/nav[2]/div/div[1]/div[2]/div/div/div/div[3]/ul/li[2]')
    transaction_btn.click()
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, '/html/body/div/main/div[2]/div[2]/div[2]/div/table'))
    )
    driver.save_screenshot('screen.png')
finally:
    # driver.quit()
    pass
