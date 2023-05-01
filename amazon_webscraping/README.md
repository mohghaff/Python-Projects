Selenium Web Scraper for Amazon.ca Programming Books

Introduction

This Python script uses Selenium and Chrome WebDriver to scrape book titles and prices for programming books on Amazon.ca. It then creates a Pandas DataFrame with the scraped data and saves it to a CSV file.

Code Overview

The Service class is imported from selenium.webdriver.chrome.service to create a new Chrome WebDriver service.
The webdriver module is imported from selenium to create a new Chrome WebDriver instance.
The pd alias is used for the pandas module.
The time module is imported to add a delay to allow the page to fully load.
The script navigates to the Amazon.ca page for programming books using the get() method.
The script waits for the page to fully load using time.sleep().
The script finds all book title elements and adds them to the list of books using the find_elements() method.
The script finds all book price elements and adds them to the list of prices using the find_elements() method.
The script ensures that the length of book_titles and book_prices are the same by adding None or empty string as necessary.
The script creates a Pandas DataFrame with the scraped data and saves it to a CSV file.
The script prints the length of the book_titles and book_prices lists for debugging purposes.
The Chrome WebDriver instance is closed using the quit() method.
