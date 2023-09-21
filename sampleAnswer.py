import requests
import re

# Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}

def compare_prices(product_laughs, product_glomark):
    # Acquire the web pages which contain product Price
    response_laughs = requests.get(product_laughs, headers=user_agent)
    response_glomark = requests.get(product_glomark, headers=user_agent)

    # Extract the HTML content
    content_laughs = response_laughs.content.decode('utf-8')
    content_glomark = response_glomark.content.decode('utf-8')

    # Extract prices using regular expressions
    price_laughs = extract_price(content_laughs)
    price_glomark = extract_price(content_glomark)

    if price_laughs is None or price_glomark is None:
        print("Failed to extract prices.")
        return

    # Print product names and prices
    print('Laughs  Rs.:', price_laughs)
    print('Glomark Rs.:', price_glomark)

    if price_laughs > price_glomark:
        print('Glomark is cheaper Rs.:', price_laughs - price_glomark)
    elif price_laughs < price_glomark:
        print('Laughs is cheaper Rs.:', price_glomark - price_laughs)
    else:
        print('Price is the same')

def extract_price(text):
    # Use regular expression to find the price
    price_match = re.search(r'Rs\.\s*([\d.,]+)', text)
    if price_match:
        return float(price_match.group(1).replace(',', ''))
    return None

# Test case
laughs_coconut = 'https://scrape-sm1.github.io/site1/COCONUT%20market1super.html'
glomark_coconut = 'https://glomark.lk/coconut/p/11624'
compare_prices(laughs_coconut, glomark_coconut)
#%%
