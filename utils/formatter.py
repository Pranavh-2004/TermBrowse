import textwrap
from rich import print as rprint
from termcolor import colored 

def print_boxed(text, width=110):
    lines = textwrap.wrap(text, width=width)
    box_top = "┏" + "━" * width + "┓"
    box_bottom = "┗" + "━" * width + "┛"
    print(box_top)
    for line in lines:
        print("┃" + line.ljust(width) + "┃")
    print(box_bottom)

def print_list(items):
    for idx, item in enumerate(items, 1):
        print(f"[{idx}] {item[0]}")

def print_search_results(results):
    rprint("[bold underline green]Search Results:[/bold underline green]")
    for idx, (title, _) in enumerate(results, 1):
        rprint(f"[{idx}] {title}")

def print_links(links):
    rprint("[bold underline cyan]Links on Page:[/bold underline cyan]")
    for idx, (text, _) in enumerate(links, 1):
        rprint(f"[{idx}] {text}")

def paginate_text(text, lines_per_page=20):
    lines = text.split('\n')
    total = len(lines)
    i = 0
    while i < total:
        for line in lines[i:i+lines_per_page]:
            print(line)
        i += lines_per_page
        if i < total:
            cmd = input("🔽 Press Enter to continue, 'q' to quit: ").strip().lower()
            if cmd == 'q':
                break

def print_links(links, state, per_page=10):
    print("🔗 Links on this page:")

    total = len(links)
    for i in range(0, total, per_page):
        chunk = links[i:i + per_page]
        for j, (text, url) in enumerate(chunk, start=i + 1):
            visited = state.is_visited(url)
            prefix = "✅" if visited else "⬜"
            print(f"{prefix} [{j}] {text.strip() or url}")
        
        if i + per_page < total:
            response = input("🔽 Press Enter to continue, 'q' to stop: ").strip().lower()
            if response == "q":
                break