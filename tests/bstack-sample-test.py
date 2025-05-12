import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_example(selenium):
    selenium.get('https://bstackdemo.com/')

    # locating product on webpage and getting name of the product
    productText = selenium.find_element(By.XPATH, '//*[@id="1"]/p').text

    # clicking the 'Add to cart' button
    selenium.find_element(By.XPATH, '//*[@id="1"]/div[4]').click()

    # waiting until the Cart pane has been displayed on the webpage
    selenium.find_element(By.CLASS_NAME, 'float-cart__content')

    # locating product in cart and getting name of the product in cart
    productCartText = selenium.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]').text

    # checking whether product has been added to cart by comparing product name
    assert productCartText == productText

def test_product_sorting(selenium):
    selenium.get('https://bstackdemo.com/')

    # Find and click on the sort dropdown
    sort_dropdown = selenium.find_element(By.CSS_SELECTOR, '.sort select')
    select = Select(sort_dropdown)

    # Select "Lowest to Highest" option
    select.select_by_visible_text('Lowest to Highest')

    # Wait for the page to update after sorting
    WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.shelf-item'))
    )

    # Get the prices of the first two items to verify sorting
    first_item_price = float(selenium.find_element(By.XPATH, '//*[@id="1"]/div[3]/span').text.replace('$', ''))
    second_item_price = float(selenium.find_element(By.XPATH, '//*[@id="2"]/div[3]/span').text.replace('$', ''))

    # Verify that the sorting works correctly (first item should be cheaper than or equal to second)
    assert first_item_price <= second_item_price, "Products are not sorted correctly by price"
