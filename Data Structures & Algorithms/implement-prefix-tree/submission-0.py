class PrefixTree:

    def __init__(self):
        self.prefix_tree = {}

    def insert(self, word: str) -> None:
        curr_layer = self.prefix_tree

        for c in word:
            if c in curr_layer:
                curr_layer = curr_layer[c]
            else:
                curr_layer[c] = {}
                curr_layer = curr_layer[c]
        
        curr_layer["@"] = {}

    def search(self, word: str) -> bool:
        curr_layer = self.prefix_tree

        for c in word:
            if c in curr_layer:
                curr_layer = curr_layer[c]
            else:
                return False
        
        return "@" in curr_layer

    def startsWith(self, prefix: str) -> bool:
        curr_layer = self.prefix_tree

        for c in prefix:
            if c in curr_layer:
                curr_layer = curr_layer[c]
            else:
                return False
        
        return True
        