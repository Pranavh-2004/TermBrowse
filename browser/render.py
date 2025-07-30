from readability import Document
from bs4 import BeautifulSoup
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()

def render_page(html):
    """
    Extract and display the readable content of a page using readability-lxml.
    """
    try:
        doc = Document(html)
        title = doc.short_title()
        summary_html = doc.summary()
        soup = BeautifulSoup(summary_html, 'html.parser')
        content = soup.get_text(separator='\n', strip=True)

        # Display with rich
        console.print(Panel.fit(f"[bold green]{title}[/bold green]", title="📰 Readable Page"))
        snippet = "\n".join(content.splitlines()[:40])  # Limit display
        console.print(Markdown(snippet or "_No content extracted._"))
        console.rule("[dim]End of Page")

    except Exception as e:
        console.print(f"[red]❌ Error rendering page:[/red] {e}")