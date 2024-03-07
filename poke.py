import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://web.facebook.com/pokes?notif_id=1709327817170390&notif_t=poke&ref=notif'

def click_button(driver):
    try:
        
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Poke Back')]")))
        button.click()
        print("Button clicked!")
    except Exception as e:
        print("Failed to click button:", e)


def reload_page(driver):    
    driver.refresh()
    print("Page reloaded!")


def main():
    
    driver = webdriver.Chrome()
    
    
    driver.get(url)
    
    try:
        while True:
            
            click_button(driver)
            reload_page(driver)
            
            
            import random
            
            time.sleep(random.randint(1,20))
    except KeyboardInterrupt:
        
        driver.quit()

if __name__ == "__main__":
    main()
