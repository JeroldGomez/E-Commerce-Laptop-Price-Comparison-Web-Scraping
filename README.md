# E-Commerce Laptop Price Comparison Web Scraping

## Overview
E-Commerce Laptop Price Comparison Web Scraping is a Python project that scrapes laptop prices and details from Amazon. The script extracts essential information like product title, price, and brand, and stores it in a pandas DataFrame for easy comparison.

## Features
- Scrapes laptop prices and details from Amazon.
- Extracts and formats product details including ASIN, brand, title, price, and date.
- Stores the extracted data in a pandas DataFrame.
- Includes a section for scraping product reviews (currently commented out).

## Installation

Clone the repository:
```
git clone https://github.com/JeroldGomez/E-Commerce-Laptop-Price-Comparison-Web-Scraping.git
cd E-Commerce-Laptop-Price-Comparison-Web-Scraping
```

Create and activate a virtual environment (optional but recommended):
```
python -m venv venv
source venv\Scripts\activate
```

Install the required dependencies:
```
pip install requests-html pandas
```

## Usage

Run the script:
```
python script.py
```
The script will scrape the laptop prices and details from Amazon and store them in a pandas DataFrame.

## Example
Here is an example of how to use the script:
```python
from requests_html import HTMLSession
import datetime
import pandas as pd

session = HTMLSession()

url = 'https://www.amazon.com/s?k=laptop&ref=nb_sb_noss_2'
r = session.get(url)
r.html.render()

product_links = r.html.find('.s-underline-link-text')
asins = set()

for link in product_links:
    product_url = link.attrs['href']
    full_product_url = 'https://www.amazon.com' + product_url
    try:
        asin = full_product_url.split('/dp/')[1].split('/')[0]
        asins.add(asin)
    except IndexError:
        pass

websites_list = []
asins_list = []
brands_list = []
titles_list = []
prices_list = []
dates_list = []

for asin in asins:
    r = session.get(f'https://www.amazon.com/dp/{asin}?th=1')
    r.html.render(sleep=1)
    
    price = format(float(r.html.find('.a-price-whole')[0].text), '.2f').strip()
    title = r.html.find('#productTitle')[0].text.strip()
    date = datetime.datetime.today()
    brand = title.split(' ')[0]
    website = full_product_url.split('www.')[1].split('.com/')[0]
    
    websites_list.append(website)
    asins_list.append(asin)
    brands_list.append(brand)
    titles_list.append(title.encode('utf-8', 'ignore').decode('utf-8'))
    prices_list.append(price)
    dates_list.append(date)

data = {
    'Website': websites_list,
    'ASIN': asins_list,
    'Brand': brands_list,
    'Title': titles_list,
    'Price': prices_list,
    'Date': dates_list
}

df = pd.DataFrame(data)
print(df)
```
