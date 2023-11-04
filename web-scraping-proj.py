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

# Find all product links on the page
product_links = r.html.find('.s-underline-link-text')

# Extract ASINs from the links and store them in a set to eliminate duplicates
asins = set()
for link in product_links:
    product_url = link.attrs['href']
    try:
        asin = product_url.split('/dp/')[1].split('/')[0]
        asins.add(asin)
    except IndexError:
        # Handle the error and continue the loop
        pass

# Product Details Section

for asin in asins:
    r = session.get(f'https://www.amazon.com/dp/{asin}?th=1')

    r.html.render(sleep = 1)

    price = format(float(r.html.find('.a-price-whole')[0].text), '.2f').strip()
    title = r.html.find('#productTitle')[0].text.strip()
    date = datetime.datetime.today()
    brand = title.split(' ')[0]

    print('ASIN:', asin)
    print('Brand:', brand)
    print('Title:', title.encode('utf-8', 'ignore').decode('utf-8'))
    print('Price:', price)
    print('Date:', date)
    print('\n')


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



