from bs4 import BeautifulSoup

def extract_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for i, a in enumerate(soup.find_all('a', href=True), 1):
        text = a.get_text(strip=True) or a['href']
        links.append((i, text[:100], a['href']))
    return links