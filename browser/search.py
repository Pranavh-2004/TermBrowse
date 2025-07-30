import requests
from bs4 import BeautifulSoup

def duckduckgo_search(query, max_results=5):
    """
    Perform a DuckDuckGo search and return a list of (title, link) tuples.

    Args:
        query (str): Search query.
        max_results (int): Maximum number of results to return.

    Returns:
        list: List of (title, href) tuples.
    """
    url = 'https://html.duckduckgo.com/html/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    data = {'q': query}

    try:
        response = requests.post(url, data=data, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ DuckDuckGo search failed: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    for a in soup.select('.result__a'):
        title = a.get_text(strip=True)
        href = a.get('href')
        if title and href:
            results.append((title, href))
        if len(results) >= max_results:
            break

    if not results:
        print("⚠️ No results found.")
    return results

def perform_search(query, max_results=5):
    """
    Wrapper function to perform a search using the selected engine.
    """
    return duckduckgo_search(query, max_results)