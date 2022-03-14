from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

#driver = webdriver.Chrome()

PATH="https://helyesiras.mta.hu/helyesiras/default/suggest"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

options = webdriver.ChromeOptions()
options.headless = True
#options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
#options.add_argument("--disable-extensions")
#options.add_argument("--proxy-server='direct://'")
#options.add_argument("--proxy-bypass-list=*")
#options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')

def helyesiras(search):
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

    driver.get(PATH)

    driver.implicitly_wait(2)


    id_box=driver.find_element_by_name('word')

    id_box.send_keys(search)
    id_box.submit()


    res= driver.find_element_by_class_name('result')

    result_text=res.text
    driver.close()  


    return(result_text)


