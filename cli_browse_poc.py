import requests
from bs4 import BeautifulSoup
from readability import Document
from rich.console import Console
from rich.markdown import Markdown

console = Console()


def search_duckduckgo(query):
    url = 'https://html.duckduckgo.com/html/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.post(url, data={'q': query}, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    results = []
    for a in soup.select('.result__a'):
        href = a.get('href')
        title = a.get_text(strip=True)
        results.append((title, href))
        if len(results) >= 5:
            break
    return results


def fetch_and_render_page(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        doc = Document(response.text)
        title = doc.short_title()
        summary_html = doc.summary()
        summary_text = BeautifulSoup(summary_html, 'html.parser').get_text()
        return f"# {title}\n\n{summary_text}"
    except Exception as e:
        return f"Failed to fetch page: {e}"


def main():
    console.print("[bold cyan]CLI Browser Search[/bold cyan]")
    query = console.input("🔍 Search: ")

    console.print("\n[bold yellow]Search Results:[/bold yellow]")
    results = search_duckduckgo(query)

    if not results:
        console.print("No results found.")
        return

    for i, (title, _) in enumerate(results, 1):
        console.print(f"[{i}] {title}")

    choice = console.input("\nEnter number to open: ")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(results):
        console.print("[red]Invalid choice[/red]")
        return

    _, link = results[int(choice) - 1]
    console.print(f"\n[bold green]Fetching:[/bold green] {link}\n")

    content = fetch_and_render_page(link)
    console.print(Markdown(content))


if __name__ == '__main__':
    main()