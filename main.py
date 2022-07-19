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

    results_final = ""
    for i in results:
        results_final += i.text
        results_final += "\n" + str(i.get_attribute("href")) + "\n\n"
    driver.quit()
    return results_final 

