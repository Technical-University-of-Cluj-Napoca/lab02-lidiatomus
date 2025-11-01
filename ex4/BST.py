import urllib.request

class Node:
  
    def __init__(self, word: str):
        self.word = word
        self.left = None
        self.right = None


class BST:
    
    def __init__(self, source: str, **kwargs):
        self.root = None
        self.results = []

        words = []

        if kwargs.get("url", False):
            print(f"Fetching wordlist from URL: {source}")
            try:
                response = urllib.request.urlopen(source)
                text = response.read().decode("utf-8")
                words = text.splitlines()
            except Exception as e:
                print("Error loading from URL:", e)
                return

        elif kwargs.get("file", False):
            print(f"Loading wordlist from file: {source}")
            try:
                with open(source, "r", encoding="utf-8") as f:
                    words = [line.strip() for line in f if line.strip()]
            except FileNotFoundError:
                print("Error: file not found.")
                return
        else:
            print("Please specify url=True or file=True when loading.")
            return

        words = sorted(set(words))
        print(f"Loaded {len(words)} words.")

        self.root = self._build_balanced(words, 0, len(words) - 1)

    pass

    def _build_balanced(self, words, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = Node(words[mid])
        node.left = self._build_balanced(words, start, mid - 1)
        node.right = self._build_balanced(words, mid + 1, end)
        return node

    pass

    def autocomplete(self, prefix: str):
        self.results = []
        self._collect(self.root, prefix)
        return self.results

    pass

    def _collect(self, node: Node, prefix: str):
        if node is None:
            return

        self._collect(node.left, prefix)

        if node.word.startswith(prefix):
            self.results.append(node.word)

        self._collect(node.right, prefix)

    pass
