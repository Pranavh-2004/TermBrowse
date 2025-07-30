class History:
    def __init__(self):
        self.stack = []
        self.forward_stack = []

    def visit(self, url):
        if self.stack:
            self.forward_stack.clear()
        self.stack.append(url)

    def back(self):
        if len(self.stack) > 1:
            self.forward_stack.append(self.stack.pop())
            return self.stack[-1]
        return None

    def forward(self):
        if self.forward_stack:
            url = self.forward_stack.pop()
            self.stack.append(url)
            return url
        return None

    def current(self):
        return self.stack[-1] if self.stack else None