import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    """
    Fetches the content of a webpage.
    
    :param url: URL to fetch content from.
    :return: BeautifulSoup object containing the parsed HTML content.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

    return BeautifulSoup(response.text, 'html.parser')

def scrape_headings(soup):
    """
    Extracts headings from a BeautifulSoup object.
    
    :param soup: BeautifulSoup object.
    :return: List of headings.
    """
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    return [heading.get_text().strip() for heading in headings]

def scrape_links(soup):
    """
    Extracts links from a BeautifulSoup object.

    :param soup: BeautifulSoup object.
    :return: List of URLs.
    """
    links = soup.find_all('a', href=True)
    return [link['href'] for link in links]

def scrape_images(soup):
    """
    Extracts image URLs from a BeautifulSoup object.

    :param soup: BeautifulSoup object.
    :return: List of image URLs.
    """
    images = soup.find_all('img')
    return [image['src'] for image in images if 'src' in image.attrs]

def scrape_text(soup):
    """
    Extracts textual content from a BeautifulSoup object.

    :param soup: BeautifulSoup object.
    :return: String containing all the text.
    """
    return soup.get_text()

def scrape(url, data_types):
    """
    Main function to scrape various data types from a URL.

    :param url: URL to scrape.
    :param data_types: List of data types to scrape (e.g., ['headings', 'links']).
    :return: Dictionary containing scraped data.
    """
    results = {}
    soup = fetch_page(url)

    if soup:
        if 'headings' in data_types:
            results['headings'] = scrape_headings(soup)
        if 'links' in data_types:
            results['links'] = scrape_links(soup)
        if 'images' in data_types:
            results['images'] = scrape_images(soup)
        if 'text' in data_types:
            results['text'] = scrape_text(soup)

    return results
