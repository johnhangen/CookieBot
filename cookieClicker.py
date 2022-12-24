from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

placeholder = True

numCookies = driver.find_element_by_xpath('//*[(@id = "cookies")]')
bigCookie = driver.find_element_by_xpath('//*[(@id = "bigCookie")]')

driver.implicitly_wait(5) 

def cookie_count():
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

while (placeholder):

    for click in range(1000):
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