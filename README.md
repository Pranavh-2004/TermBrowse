# TermBrowse

**TermBrowse** is a lightweight command-line web browser designed for productivity and minimalism. It allows you to search the web, view readable text content, follow links, and manage bookmarks — all from your terminal.

---

## 📦 Features

* 🔍 Web search using DuckDuckGo
* 🌐 Browse simplified readable web pages
* 🧭 Navigate history: `:back`, `:forward`
* 🔖 Bookmark support: `:bookmark`, `:bookmarks`
* 🔗 Follow page links with `link <n>` or `l <n>`
* 📄 Paginated article view
* 🌈 Highlights visited links

---

## 🧑‍💻 Usage

### 🔧 Installation

```bash
# Clone the repository
$ git clone https://github.com/your-username/termbrowse.git
$ cd termbrowse

# Create and activate a virtual environment
$ python3 -m venv venv
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt
```

### 🚀 Running TermBrowse

```bash
$ python cli_browse.py
```

You’ll be greeted with a prompt:

```
🧭 CLI Browser
Type a search query or command:
  - :back, :forward, :bookmark, :bookmarks, :exit
  - link <n> or l <n> to open a link on current page
```

---

## 📂 Project Structure

```
TermBrowse/
├── browser/              # Core browsing logic
│   ├── fetch.py          # Page fetching and readability parsing
│   ├── history.py        # Browsing history management
│   ├── links.py          # Link utilities
│   ├── render.py         # (optional extension)
│   └── search.py         # DuckDuckGo search integration
├── cli_browse.py         # Main CLI launcher
├── cli_browse_poc.py     # Proof-of-concept legacy script
├── data/
│   └── bookmarks.json    # Bookmarked URLs
├── tests/                # Unit tests
│   ├── test_render.py
│   └── test_search.py
├── utils/
│   ├── formatter.py      # Link display, text pagination, color formatting
│   ├── bookmarks.py      # Bookmark storage and retrieval
│   └── state.py          # Session state manager
├── requirements.txt      # Dependencies
├── LICENSE
└── README.md             # You’re here!
```

---

## ✅ To-Do / Roadmap

* [x] Integrated readability parsing
* [x] Paginated terminal viewer
* [x] Bookmarks and visited link storage
* [ ] Tabbed browsing
* [ ] Image or media previews
* [ ] Custom themes (light/dark)

---

## 🧪 Testing

Run tests using:

```bash
$ python -m unittest discover tests
```

---

## 🧠 Inspiration

* [w3m](http://w3m.sourceforge.net/)
* [lynx](https://lynx.invisible-island.net/)
* [readability-lxml](https://github.com/buriy/python-readability)

---

## ⚖️ License

MIT License. See `LICENSE` file for details.

---

## 👨‍🚀 Author

**Pranav Hemanth** — [@pranav-hemanth](https://github.com/pranav-hemanth)
