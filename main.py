"""
main.py - Sample Web Scraper Boilerplate
Author: Irfana Aslam
Email: irfanaaslam69@gmail.com
Description: Demonstrates basic web scraping workflow using Requests, BeautifulSoup, and Pandas.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# 🌐 Step 1: Define the target URL
URL = "https://quotes.toscrape.com"  # A free website for practicing web scraping

def scrape_quotes():
    """Scrape quotes, authors, and tags from the example website."""
    response = requests.get(URL)
    
    if response.status_code != 200:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        return None

    # 🥣 Step 2: Parse the HTML
    soup = BeautifulSoup(response.text, "lxml")

    # 📑 Step 3: Extract data
    data = []
    for quote_block in soup.find_all("div", class_="quote"):
        quote = quote_block.find("span", class_="text").get_text(strip=True)
        author = quote_block.find("small", class_="author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in quote_block.find_all("a", class_="tag")]

        data.append({
            "quote": quote,
            "author": author,
            "tags": ", ".join(tags)
        })

    # 📊 Step 4: Save to DataFrame
    df = pd.DataFrame(data)
    return df


if __name__ == "__main__":
    df = scrape_quotes()
    if df is not None:
        print("✅ Scraping complete. Sample output:")
        print(df.head())

        # 💾 Save results
        df.to_csv("quotes.csv", index=False, encoding="utf-8")
        print("📂 Data saved to quotes.csv")
