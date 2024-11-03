# Selenium Web Scraping Amazon Products

## Introduction
This project uses Selenium to scrape product information from Amazon based on a search query. It extracts details such as product titles, prices, images, and links, then saves this data into a CSV file.

## Installation
1. Ensure you have Python installed on your machine.
2. Install the required dependencies using pip:
pip install selenium
3. Download the appropriate web driver (e.g., ChromeDriver) and ensure it's in your system PATH.

## Usage
Run the script to start scraping. It will navigate to Amazon, perform a search for "ram", and extract product details. The extracted information is saved in a CSV file named `data.csv`.

## Features
- Automated navigation through Amazon search results.
- Extraction of product titles, prices, images, and links.
- Data stored in a CSV file using a semicolon as a delimiter.

## Code Overview
The main components of the script include:
- **CSV Initialization**: Creates a CSV file and writes headers.
- **Data Extraction**: Loops through search results to gather product information.
- **Pagination Handling**: Clicks the "Next" button to navigate through multiple pages of results.

## Conclusion
This Selenium web scraping project provides a straightforward way to gather product information from Amazon for further analysis or personal use. Customize the search query and data handling as needed.
