from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd

website = 'https://www.worldometers.info/world-population/world-population-by-year/'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get(website)


all_populations = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div[1]/table')

year = []
world_population = []
net_change = []
density = []

for populations in all_populations.find_elements(By.XPATH, '//tr'):
    all_years = [item.text for item in populations.find_elements(By.XPATH, './/td[1]')]
    year.append(all_years)
    print(*all_years)
    world = [item.text for item in populations.find_elements(By.XPATH, './/td[2]')]
    world_population.append(world)
    net = [item.text for item in populations.find_elements(By.XPATH, './/td[3]')]
    net_change.append(net)
    densy = [item.text for item in populations.find_elements(By.XPATH, './/td[4]')]
    density.append(densy)
driver.quit()

df = pd.DataFrame({'year': year, 'world_population': world_population, 'net_change': net_change, 'density': density})
df.to_csv('population_data.csv', index=False)
print(df)
