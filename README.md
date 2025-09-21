
Book Scraper
This is a Python script designed to scrape book information from the fictional web scraping sandbox website, http://books.toscrape.com/. The script is a simple, single-file application that demonstrates the basic principles of web scraping using Python.

Features
Scrapes Book Data: Extracts the title, price, and star rating for each book on the main page.

Saves to CSV: Automatically saves the scraped data into a structured CSV file for easy viewing and analysis.

User-Agent Header: Includes a User-Agent header in the request to mimic a standard web browser, which can help prevent being blocked by some websites.

Robust Error Handling: Contains try...except blocks to handle common issues like network errors and unexpected website changes.

Requirements
The script uses the requests and beautifulsoup4 libraries. You can install them using pip:

pip install requests beautifulsoup4

Usage
Save the script: Save the provided Python code as book_scraper.py.

Run the script: Open your terminal or command prompt and navigate to the directory where you saved the file. Run the script using the following command:

python book_scraper.py

The script will fetch the data, and if successful, a file named books.csv will be created in the A:/Python/Web_scraping/ directory.

Output
The books.csv file will contain three columns: title, price, and rating.
