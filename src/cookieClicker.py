import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Language(driver, wait, Xpath:str = '//*[@id="langSelect-EN"]'):
    """Selects Language so we can start the game

    Args:
        driver (driver): Firefox driver element
        Xpath (str, optional): xpath to english. Defaults to '//*[@id="langSelect-EN"]'.
    """
    wait.until(lambda driver: driver.find_element_by_xpath(Xpath))
    driver.find_element_by_xpath(Xpath).click()


def InitCookies(driver, wait):
    try:
        driver.implicitly_wait(5)
        wait.until(lambda driver: driver.find_element_by_xpath('//*[(@id = "bigCookie")]'))

        bigCookie = driver.find_element_by_xpath('//*[(@id = "bigCookie")]')
        numCookies = driver.find_element_by_xpath('//*[(@id = "cookies")]')
        return bigCookie, numCookies
    except:
        InitCookies(driver, wait)


def cookie_count(numCookies):
    words = numCookies.text
    if "ion" in words:
        if "million" in words:
            return int((numCookies.text.split(" ")[0]).replace(",",""))*1000000
        elif "billion" in words:
            return int((numCookies.text.split(" ")[0]).replace(",",""))*1000000000
        elif "trillion" in words:
            return int((numCookies.text.split(" ")[0]).replace(",",""))*1000000000000
        elif "quadrillion" in words:
            return int((numCookies.text.split(" ")[0]).replace(",",""))*1000000000000000
        elif "zillion " in words:
            return int((numCookies.text.split(" ")[0]).replace(",",""))*1000000000000000000
    else:
        return int((numCookies.text.split(" ")[0]).replace(",",""))



def main():
    # Driver setup
    os.chdir(r'src\geckodriver')
    driver = webdriver.Firefox()
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    wait = WebDriverWait(driver, 15)

    placeholder = True

    Language(driver, wait)

    bigCookie, numCookies = InitCookies(driver, wait)

    # main loop
    while (placeholder):

        for click in range(100):
            bigCookie.click()

        try:
            driver.find_element_by_xpath(f'//*[(@id = "upgrade{0}")]').click()
        except:
            pass

        for x in range(20,-1,-1):
            try:
                loop = True
                count = 0
                while loop and count <= 10:
                    count = count + 1
                    driver.find_element_by_xpath(f'//*[(@id = "product{x}")]').click()
            except:
                loop = False

    driver.close()


if __name__ == "__main__":
    main()