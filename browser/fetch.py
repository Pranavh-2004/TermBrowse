'''
import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    """
    Fetch and parse a webpage.

    Args:
        url (str): URL to fetch.

    Returns:
        dict: {
            'title': str,
            'text': str,
            'links': list of (label, absolute_url)
        }
    """
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ Failed to fetch page: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Get title
    title = soup.title.string.strip() if soup.title else 'No Title'

    # Get visible text
    for script in soup(["script", "style", "noscript"]):
        script.extract()
    text = soup.get_text(separator='\n')
    lines = [line.strip() for line in text.splitlines()]
    text = '\n'.join(line for line in lines if line)

    # Get links
    links = []
    for a in soup.find_all('a', href=True):
        label = a.get_text(strip=True)
        href = requests.compat.urljoin(url, a['href'])  # Make absolute
        if label and href:
            links.append((label, href))

    return {
        'title': title,
        'text': text,
        'links': links
    }
    '''

import requests
from bs4 import BeautifulSoup
from readability import Document

def fetch_page(url):
    """
    Fetch and parse a webpage using readability to extract main content.

    Args:
        url (str): URL to fetch.

    Returns:
        dict: {
            'title': str,
            'text': str,
            'links': list of (label, absolute_url)
        }
    """
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ Failed to fetch page: {e}")
        return None

    # Use Readability to extract main article
    doc = Document(response.text)
    title = doc.short_title()
    summary_html = doc.summary()

    soup = BeautifulSoup(summary_html, 'html.parser')

    # Extract clean text from summary
    for tag in soup(['script', 'style', 'noscript']):
        tag.decompose()

    text = soup.get_text(separator='\n')
    lines = [line.strip() for line in text.splitlines()]
    text = '\n'.join(line for line in lines if line)

    # Extract links from summary
    links = []
    for a in soup.find_all('a', href=True):
        label = a.get_text(strip=True)
        href = requests.compat.urljoin(url, a['href'])  # Make absolute
        if label and href:
            links.append((label, href))

    return {
        'title': title,
        'text': text,
        'links': links
    }