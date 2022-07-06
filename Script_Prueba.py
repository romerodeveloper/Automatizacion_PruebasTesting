from selenium import webdriver

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.maximize_window()

driver.get("https://www.netflix.com/co/login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse")

driver.close()