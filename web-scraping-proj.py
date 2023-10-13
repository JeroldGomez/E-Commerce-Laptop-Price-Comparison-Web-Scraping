from requests_html import HTMLSession
import datetime


# HTML session
session = HTMLSession()

# Amazon search results URL
url = 'https://www.amazon.com/s?k=laptop&ref=nb_sb_noss_2'

# GET request to the URL
r = session.get(url)

# Parse the page content
r.html.render()

# Extracting ASINS Section

'''
# Find all product links on the page
product_links = r.html.find('.s-underline-link-text')

# Extract ASINs from the links
asins = []
for link in product_links:
    href = link.attrs['href']
    try:
        asin = href.split('/dp/')[1].split('/')[0]
        asins.append(asin)
    except IndexError:
        pass

# Print the ASINs
for asin in asins:
    print(asin)
'''

# Product Details Section

'''

for asin in asins:
    r = s.get(f'https://www.amazon.com/dp/{asin}?th=1')

    r.html.render(sleep = 1)

    price = format(float(r.html.find('.a-price-whole')[0].text), '.2f').strip()
    title = r.html.find('#productTitle')[0].text.strip()
    asin = asin
    date = datetime.datetime.today()

    print(asin)
    print(title)
    print(price)
    print(date)
    print('\n')
'''


# Product Reviews Section

'''
class Reviews:
    def __init__(self, asin) -> None:
        self.session = HTMLSession()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
        self.asin = asin
        self.url = f'https://www.amazon.com/product-reviews/{self.asin}/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&pageNumber='

    def pagination(self, page):
        r = self.session.get(self.url + str(page))
        r.html.render(sleep = 1)
        if not r.html.find('div[data-hook=review]'):
            return False
        else:
            return r.html.find('div[data-hook=review]')

    def parse(self, reviews):
        total = []
        for review in reviews:
            product_review_title = review.find('a[data-hook=review-title]', first=True).text
            product_review_rating = float(review.find('i[data-hook=review-star-rating] span', first = True).text.replace('out of 5 stars', '').strip())
            product_review_body = review.find('span[data-hook=review-body] span', first = True).text.replace('\n', '').strip()

            data = {
                'title': product_review_title[19:],
                'rating': product_review_rating,
                'review': product_review_body[:100] # changing 100 characters to none for final
            }

            total.append(data)
        return total


if __name__ == '__main__':
    amz = Reviews('B0CCVDGLTV')
    reviews = amz.pagination(1)
    print(amz.parse(reviews))
'''



