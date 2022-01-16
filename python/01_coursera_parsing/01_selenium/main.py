from selenium import webdriver


def get_tags():
    driver = webdriver.Chrome()
    driver.get("https://quotes.toscrape.com/js-delayed/")

    tags = set()
    for i in range(1, 11):
        driver.get(f"https://quotes.toscrape.com/js-delayed/page/{i}/")
        element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".tag"))
        )
        tags_raw = driver.find_elements_by_xpath("//*[@class='tag']")
    
        for tag_raw in tags_raw:
            tags.add(tag_raw.text)
    return sorted(tags)


if __name__ == "__main__":
    get_tags()
