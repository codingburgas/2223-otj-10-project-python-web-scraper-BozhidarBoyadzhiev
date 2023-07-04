import requests
import menu
import os
from bs4 import BeautifulSoup

# Clear console
clear = lambda: os.system('cls')

def filter(city, manufacturer, gcard):
    clear()
    url = f'https://ardes.bg/kompyutri/nastolni-kompyutri/{manufacturer}/{gcard}/za-igri-gaming?gclid=EAIaIQobChMI-vmdobz0_wIVOYODBx2WkgsNEAAYASACEgK4H_D_BwE&town={city}'
    
    r = requests.get(url)

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    # If there are not any products, but if found to show to the user
    try:
        no_found = soup.find('div', class_='alert-no-found').text.strip()
    except:
        # Description of the product
        products = soup.find_all('div', class_='product')

        # Product's parameters
        product_parameters = soup.find_all("ul", class_='parameters')

        # Counter
        computer_number = 1

        # Show each computer
        for product in products:
            product_name = product.find('div', class_='isTruncated').text.strip()
            product_price = product.find('div', class_='price').text.strip()
            product_parameters = product.find('ul', class_='parameters')

            list_items = []
            for li in product_parameters.find_all('li'):
                list_items.append(li.text.strip())
            print(f"{computer_number}. Product: {product_name}\n"
                f"\tPrice: {product_price[:-4]} лв\n"
                f"\tProcessor: {list_items[0]}\n"
                f"\tGraphics card: {list_items[1]}\n"
                f"\tRAM: {list_items[2]}\n"
                f"\tSSD: {list_items[3]}\n\n")
            computer_number += 1
        shope_more = input("Do you wish to continue shopping? (y/n): ")
        if shope_more == 'y':
            menu.menu()
        elif shope_more == 'n':
            exit()
        else:
            filter(city, manufacturer, gcard)

    # If there are not any products
    if no_found == "Няма намерени продукти по зададените критерии!":
        print(f"There are not any {manufacturer} computers with {gcard} in {city.capitalize()}.")
        shope_more = input("Do you wish to continue shopping? (y/n): ")
        if shope_more == 'y':
            menu.menu()
        elif shope_more == 'n':
            exit()
        else:
            filter(city, manufacturer, gcard)