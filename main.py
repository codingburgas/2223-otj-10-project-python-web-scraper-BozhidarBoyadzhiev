import requests
from bs4 import BeautifulSoup

r = requests.get('https://ardes.bg/kompyutri/nastolni-kompyutri/za-igri-gaming?gclid=EAIaIQobChMI-vmdobz0_wIVOYODBx2WkgsNEAAYASACEgK4H_D_BwE')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

products = soup.find_all('div', class_='product')

product_parameters = soup.find_all("ul", class_='parameters')

for product in products:
    product_name = product.find('div', class_='isTruncated').text.strip()
    product_price = product.find('div', class_='price').text.strip()
    product_parameters = product.find('ul', class_='parameters')

    list_items = []
    for li in product_parameters.find_all('li'):
        list_items.append(li.text.strip())
    print(f"Product: {product_name}\n"
          f"Price: {product_price[:-4]} лв\n"
          f"Processor: {list_items[0]}\n"
          f"Graphics card: {list_items[1]}\n"
          f"RAM: {list_items[2]}\n"
          f"SSD: {list_items[3]}\n")
    print("-----------------------")