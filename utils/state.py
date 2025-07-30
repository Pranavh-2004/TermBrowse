class AppState:
    def __init__(self):
        self.search_results = []
        self.current_url = None
        self.history = []
        self.forward_stack = []
        self.current_links = []
        self.visited_links = set()   # ✅ Track visited URLs
        self.bookmarks = []          # ✅ Store bookmarked URLs

    def add_to_history(self, url):
        if self.current_url:
            self.history.append(self.current_url)
        self.current_url = url
        self.forward_stack.clear()

    def go_back(self):
        if self.history:
            self.forward_stack.append(self.current_url)
            self.current_url = self.history.pop()
            return self.current_url
        return None

    def go_forward(self):
        if self.forward_stack:
            self.history.append(self.current_url)
            self.current_url = self.forward_stack.pop()
            return self.current_url
        return None

    def reset_navigation(self):
        self.history.clear()
        self.forward_stack.clear()
        self.current_url = None

    # ✅ Bookmark methods
    def add_bookmark(self, url):
        if url not in self.bookmarks:
            self.bookmarks.append(url)

    def get_bookmarks(self):
        return self.bookmarks

    def remove_bookmark(self, url):  # ✅ Remove bookmark
        if url in self.bookmarks:
            self.bookmarks.remove(url)

    def search_bookmarks(self, query):  # ✅ Search bookmarks
        query_lower = query.lower()
        return [url for url in self.bookmarks if query_lower in url.lower()]

    # ✅ Visited links methods
    def mark_visited(self, url):
        self.visited_links.add(url)

    def is_visited(self, url):
        return url in self.visited_links