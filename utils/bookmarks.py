import json
import os

BOOKMARKS_FILE = os.path.join(os.path.dirname(__file__), "../data/bookmarks.json")

def load_bookmarks():
    if not os.path.exists(BOOKMARKS_FILE):
        return []
    with open(BOOKMARKS_FILE, 'r') as f:
        return json.load(f)

def save_bookmarks(bookmarks):
    with open(BOOKMARKS_FILE, 'w') as f:
        json.dump(bookmarks, f, indent=2)

def add_bookmark(title, url):
    bookmarks = load_bookmarks()
    bookmarks.append({"title": title, "url": url})
    save_bookmarks(bookmarks)