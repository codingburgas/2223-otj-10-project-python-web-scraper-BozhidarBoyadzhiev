# Ardes Computer Scraper

This project is a web scraper that extracts computer information from the Ardes website. It provides a console application for users to easily browse and search for computers based on different criteria.

## Features

- Choose a city to filter available computers (Online, Varna, Sofia, Plovdiv, Burgas)
- Select a manufacturer to filter computers (Ardes, Powered by ASUS, Powered by Fractal Design, Acer, ASUS, Lenovo)
- Filter computers by graphics card (Nvidia GeForce RTX 4080, Nvidia GeForce RTX 4070, Nvidia GeForce RTX 3070, Nvidia GeForce RTX 3060, Nvidia GeForce RTX 3050, Nvidia GeForce RTX 1660)

## Getting Started

### Prerequisites

- Python 3.x
- BeautifulSoup library (`pip install beautifulsoup4`)
- Requests library (`pip install requests`)

### Installation

1. Clone the repository:

```
git clone https://github.com/codingburgas/2223-otj-10-project-python-web-scraper-BozhidarBoyadzhiev.git
```

2. Change to the project directory:

```
cd scripts
```

3. Run the application:

```
python main.py
```

## Usage

1. Choose a city option from the provided list.
2. Select a manufacturer option from the available choices.
3. Choose a graphics card option to filter the computers.
4. The application will display the filtered results, including product names, prices, and specifications.
5. You can continue shopping or exit the application.

## Acknowledgements

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Library for web scraping and parsing HTML
- [Requests](https://docs.python-requests.org/en/latest/) - Library for making HTTP requests
