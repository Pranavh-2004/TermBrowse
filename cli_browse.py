
'''
# cli_browse.py
from browser.search import perform_search
from browser.fetch import fetch_page
from browser.history import History
from utils.state import AppState
from utils.formatter import print_links, print_search_results, paginate_text

def main():
    history = History()
    state = AppState()

    print("🧭 CLI Browser")
    print("Type a search query or command:")
    print("  - :back, :forward, :bookmark, :bookmarks, :exit")
    print("  - link <n> or l <n> to open a link on current page\n")

    while True:
        user_input = input("📝 > ").strip()

        if not user_input:
            continue

        if user_input.startswith(":"):
            command = user_input[1:].lower()

            if command == "exit":
                print("👋 Goodbye!")
                break

            elif command == "back":
                prev_url = history.back()
                if prev_url:
                    print(f"🔙 Back to: {prev_url}")
                    page = fetch_page(prev_url)
                    if page:
                        print(f"\n📄 {page['title']}")
                        paginate_text(page['text'])
                        state.current_links = page['links']
                        state.mark_visited(prev_url)
                        print_links(state.current_links, state.visited_links)
                    else:
                        print("❌ Failed to fetch previous page.")
                else:
                    print("🔙 No more history.")

            elif command == "forward":
                next_url = history.forward()
                if next_url:
                    print(f"⏩ Forward to: {next_url}")
                    page = fetch_page(next_url)
                    if page:
                        print(f"\n📄 {page['title']}")
                        paginate_text(page['text'])
                        state.current_links = page['links']
                        state.mark_visited(next_url)
                        print_links(state.current_links, state.visited_links)
                    else:
                        print("❌ Failed to fetch next page.")
                else:
                    print("⏩ No forward history.")

            elif command == "bookmark":
                if history.current():
                    state.add_bookmark(history.current())
                    print(f"🔖 Bookmarked: {history.current()}")
                else:
                    print("❌ No page to bookmark.")

            elif command == "bookmarks":
                bookmarks = state.get_bookmarks()
                if bookmarks:
                    print("🔖 Bookmarks:")
                    for i, url in enumerate(bookmarks, 1):
                        print(f"[{i}] {url}")
                else:
                    print("📭 No bookmarks yet.")

            else:
                print("❌ Unknown command.")

        elif user_input.startswith("link ") or user_input.startswith("l "):
            try:
                _, num_str = user_input.split()
                index = int(num_str) - 1
                if 0 <= index < len(state.current_links):
                    link_url = state.current_links[index][1]
                    print(f"🌐 Opening: {link_url}")
                    page = fetch_page(link_url)
                    if page:
                        print(f"\n📄 {page['title']}")
                        paginate_text(page['text'])
                        state.current_links = page['links']
                        history.visit(link_url)
                        state.mark_visited(link_url)
                        print_links(state.current_links, state.visited_links)
                    else:
                        print("❌ Failed to fetch page.")
                else:
                    print("❌ Invalid link number.")
            except ValueError:
                print("❌ Usage: link <number>")

        else:
            results = perform_search(user_input)
            state.search_results = results
            print_search_results(results)

            choice = input("Enter number to open: ").strip()
            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(results):
                    selected_url = results[index][1]
                    print(f"Fetching: {selected_url}")
                    page = fetch_page(selected_url)
                    if page:
                        print(f"\n📄 {page['title']}")
                        paginate_text(page['text'])
                        state.current_links = page['links']
                        history.visit(selected_url)
                        state.mark_visited(selected_url)
                        print_links(state.current_links, state.visited_links)
                    else:
                        print("❌ Failed to fetch or render page.")
                else:
                    print("❌ Invalid choice.")
            else:
                print("❌ Not a valid number.")

if __name__ == "__main__":
    main()
'''

from browser.search import perform_search
from browser.fetch import fetch_page
from browser.history import History
from utils.state import AppState
from utils.formatter import print_links, print_search_results, paginate_text

def main():
    history = History()
    state = AppState()

    print("🧭 CLI Browser")
    print("Type a search query or command:")
    print("  - :back, :forward, :bookmark, :bookmarks, :exit")
    print("  - link <n> or l <n> to open a link on current page\n")

    while True:
        user_input = input("📝 > ").strip()

        if not user_input:
            continue

        if user_input.startswith(":"):
            command = user_input[1:].lower()

            if command == "exit":
                print("👋 Goodbye!")
                break

            elif command == "back":
                prev_url = history.back()
                if prev_url:
                    print(f"🔙 Back to: {prev_url}")
                    page = fetch_page(prev_url)
                    if page:
                        print(f"\n📄 {page['title']}")
                        paginate_text(page['text'])
                        state.current_links = page['links']
                        state.mark_visited(prev_url)
                        print_links(state.current_links, state)
                    else:
                        print("❌ Failed to fetch previous page.")
                else:
                    print("🔙 No more history.")

            elif command == "forward":
                next_url = history.forward()
                if next_url:
                    print(f"⏩ Forward to: {next_url}")
                    page = fetch_page(next_url)
                    if page:
                        print(f"\n📄 {page['title']}")
                        paginate_text(page['text'])
                        state.current_links = page['links']
                        state.mark_visited(next_url)
                        print_links(state.current_links, state)
                    else:
                        print("❌ Failed to fetch next page.")
                else:
                    print("⏩ No forward history.")

            elif command == "bookmark":
                if history.current():
                    state.add_bookmark(history.current())
                    print(f"🔖 Bookmarked: {history.current()}")
                else:
                    print("❌ No page to bookmark.")

            elif command == "bookmarks":
                bookmarks = state.get_bookmarks()
                if bookmarks:
                    print("🔖 Bookmarks:")
                    for i, url in enumerate(bookmarks, 1):
                        print(f"[{i}] {url}")
                else:
                    print("📭 No bookmarks yet.")

            else:
                print("❌ Unknown command.")

        elif user_input.startswith("link ") or user_input.startswith("l "):
            try:
                _, num_str = user_input.split()
                index = int(num_str) - 1
                if 0 <= index < len(state.current_links):
                    link_url = state.current_links[index][1]
                    print(f"🌐 Opening: {link_url}")
                    page = fetch_page(link_url)
                    if page:
                        print(f"\n📄 {page['title']}")
                        paginate_text(page['text'])
                        state.current_links = page['links']
                        history.visit(link_url)
                        state.mark_visited(link_url)
                        print_links(state.current_links, state)
                    else:
                        print("❌ Failed to fetch page.")
                else:
                    print("❌ Invalid link number.")
            except ValueError:
                print("❌ Usage: link <number>")

        else:
            results = perform_search(user_input)
            state.search_results = results
            print_search_results(results)

            choice = input("Enter number to open: ").strip()
            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(results):
                    selected_url = results[index][1]
                    print(f"Fetching: {selected_url}")
                    page = fetch_page(selected_url)
                    if page:
                        print(f"\n📄 {page['title']}")
                        paginate_text(page['text'])
                        state.current_links = page['links']
                        history.visit(selected_url)
                        state.mark_visited(selected_url)
                        print_links(state.current_links, state)
                    else:
                        print("❌ Failed to fetch or render page.")
                else:
                    print("❌ Invalid choice.")
            else:
                print("❌ Not a valid number.")

if __name__ == "__main__":
    main()