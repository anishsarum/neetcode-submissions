class PrefixTree:

    def __init__(self):
        self.root = {}

    def _find_node(self, prefix: str):
        curr = self.root
        for c in prefix:
            if c not in curr:
                return None
            curr = curr[c]
        return curr

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.setdefault(c, {})
        curr["@"] = True

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and "@" in node

    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None
        