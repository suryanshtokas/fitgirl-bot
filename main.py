def main(game_name):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

    driver.get("https://fitgirl-repacks.site/")
    driver.find_element(By.CLASS_NAME, "search-toggle").click()

    search_textbox = driver.find_element(By.CLASS_NAME, "search-field")
    search_textbox.send_keys(game_name)
    search_textbox.send_keys(Keys.ENTER)
    
    results = driver.find_elements(By.XPATH, "//h1/a")
    results.pop(0)

    results_list = []
    for i in results:
        results_final = [] 
        results_final.append(i.text)
        results_final.append(str(i.get_attribute("href")))  
        results_list.append(results_final)
    driver.quit()
    return results_list


def upcoming_repacks():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

    driver.get("https://fitgirl-repacks.site/")

    upcoming_games_raw = driver.find_elements(By.XPATH, "//h3/span")
    upcoming_games = []
    for i in upcoming_games_raw:
        upcoming_games.append(i.text)
    driver.quit()
    return upcoming_games[:-10]

