from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys

import time
import json

main_list = []

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
# host=appConfig.get("config", "host")
host = "https://www.myntra.com/"
brands = ["LOreal","WOW","Biotique"]
keywords = ["Hair fall shampoo","Conditioner","Shampoo"]



for keyss in keywords:
    temp_brands = brands.copy()
    print("brands",brands)
    driver.get(host)
    search_bar = driver.find_element_by_xpath("//input[@class = 'desktop-searchBar']")

    search_bar.send_keys(keyss)
    search_bar.send_keys(Keys.ENTER)
    h3_tag = driver.find_elements_by_xpath("//h3[@class = 'product-brand']")
    count = 0
    rank = {}
    for i in h3_tag:
        count = count + 1
        print(i.text)
        
        for ele in temp_brands:
            
            if (ele in i.text):
                
                rank[ele] = count
                temp_brands.remove(ele)
    print(rank)
    time.sleep(4)
    output = {"keyword":keyss,"position":rank}
    main_list.append(output)
print(main_list)
    # print(json.loads(output))

