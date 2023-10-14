import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a CSV file and write header row with semicolon as delimiter
with open("data.csv", mode='w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['Title', 'Price', 'Image', 'Link'])

def write_csv(new_data, filename='data.csv'):
    with open(filename, mode='a', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([new_data['title'], new_data['price'], new_data['image'], new_data['link']])

browser = webdriver.Chrome()
browser.get('https://www.amazon.fr/s?k=ram&__mk_fr_FR=ÅMÅŽÕÑ&crid=INXW8WWGX0NU&sprefix=ram%2Caps%2C131&ref=nb_sb_noss_1')

isNextDisabled = False

while not isNextDisabled:
    try:
        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//div[@data-component-type="s-search-result"]')))

        elem_list = browser.find_element(
            By.CSS_SELECTOR, "div.s-main-slot.s-result-list.s-search-results.sg-row")

        items = elem_list.find_elements(
            By.XPATH, '//div[@data-component-type="s-search-result"]')

        for item in items:
            title = item.find_element(By.TAG_NAME, 'h2').text
            price = "No Price Found"
            img = "No Image Found"
            link = item.find_element(
                By.CLASS_NAME, 'a-link-normal').get_attribute('href')

            try:
                price = item.find_element(
                    By.CSS_SELECTOR, '.a-price').text.replace("\n", ".")
            except:
                pass

            try:
                img = item.find_element(
                    By.CSS_SELECTOR, '.s-image').get_attribute("src")
            except:
                pass

            print("Title:", title)
            print("Price:", price)
            print("Image:", img)
            print("Link:", link, "\n")

            write_csv({
                "title": title,
                "price": price,
                "image": img,
                "link": link
            })


        next_btn = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 's-pagination-next')))

        next_class = next_btn.get_attribute('class')

        if "disabled" in next_class:
            isNextDisabled = True
        else:
            browser.find_element(By.CLASS_NAME, 's-pagination-next').click()

    except Exception as e:
        print(e, "Main Error")
        isNextDisabled = True
