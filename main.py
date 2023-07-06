from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

website = 'https://www.worldometers.info/world-population/world-population-by-year/'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get(website)


all_populations = driver.find_elements(By.TAG_NAME, 'tr')

year = []
world_population = []
net_change = []
density = []

for populations in all_populations:
    all_years = populations.find_element(By.XPATH, './td[1]').text
    year.append(all_years)
    print(all_years)
driver.quit()
