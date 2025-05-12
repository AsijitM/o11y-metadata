import random
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_example(selenium):
    selenium.get('https://bstackdemo.com/')

    # locating product on webpage and getting name of the product
    productText = selenium.find_element(By.XPATH, '//*[@id="1"]/p').text

    # clicking the 'Add to cart' button
    selenium.find_element(By.XPATH, '//*[@id="1"]/div[4]').click()

    a = random.randint(1, 1000)
    print(f'Asijit -----> {a}')
    if int(a) % 2 == 0:
        element_name = "float-cart__conten"
    else :
        element_name = "float-cart__content"

    # waiting until the Cart pane has been displayed on the webpage
    selenium.find_element(By.CLASS_NAME, element_name)

    # locating product in cart and getting name of the product in cart
    productCartText = selenium.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]').text

    # checking whether product has been added to cart by comparing product name
    assert productCartText == productText

@pytest.mark.smoke
@pytest.mark.flaky(reruns=2)
@pytest.mark.timeout(60)
def test_product_filters(selenium):
    selenium.get('https://bstackdemo.com/')

    # Click on vendor filter
    selenium.find_element(By.XPATH, '//span[text()="Apple"]').click()

    # Get the count of displayed products
    product_items = selenium.find_elements(By.CSS_SELECTOR, '.shelf-item:not(.shelf-item--hidden)')

    # Check filter is applied
    assert len(product_items) > 0, "No products displayed after applying filter"

    # Verify filtered products are from Apple
    for item in product_items:
        product_title = item.find_element(By.CSS_SELECTOR, '.shelf-item__title').text
        assert "iPhone" in product_title or "MacBook" in product_title, f"Non-Apple product found: {product_title}"
