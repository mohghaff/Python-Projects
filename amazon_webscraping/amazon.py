from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pandas as pd
import time

# create a new Chrome driver
service = Service("C:\Users\mghaf\OneDrive\Desktop\Projects\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://www.amazon.ca/s?k=programming+books&ref=nb_sb_noss")

# wait for the page to fully load for 5 seconds
time.sleep(5)

# find all book titles and prices
books = driver.find_elements("xpath", '//span[@class="a-size-base-plus a-color-base a-text-normal"]')
book_titles = [book.text for book in books]

prices = driver.find_elements("xpath", '//span[@class="a-price-whole"]')
book_prices = [price.text if price.text else None for price in prices]

# ensure both lists have the same length
while len(book_titles) != len(book_prices):
    if len(book_titles) > len(book_prices):
        book_prices.append(None)
    else:
        book_titles.append("")

# create a pandas DataFrame to store the book titles and prices
df = pd.DataFrame({"Title": book_titles, "Price": book_prices})

df["Price"] = pd.to_numeric(df["Price"].str.replace(",", ""))

df = df.sort_values("Price")

df.to_csv("programming_books.csv", index=False)

driver.quit()
