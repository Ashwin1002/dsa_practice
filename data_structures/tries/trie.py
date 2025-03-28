class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
    
    def add(self, word):
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[self.end_symbol] = True
    
    def search_level(self, current_level, current_prefix, words):
        if self.end_symbol in current_level:
            words.append(current_prefix)
        
        for k in sorted(current_level.keys()):
            if k != self.end_symbol:
                self.search_level(current_level[k], current_prefix + k, words)
        
        return words
    
    def words_with_prefix(self, prefix):
        words = []
        current = self.root
        
        for char in prefix:
            if char not in current:
                return []
            current = current[char]
        
        return self.search_level(current, prefix, words)
    
    def find_matches(self, document):
        matches = set()
        n = len(document)
        
        for i in range(n):
            current_level = self.root
            
            for j in range(i, n):
                char = document[j]
                if char not in current_level:
                    break
                
                current_level = current_level[char]
                
                if self.end_symbol in current_level:
                    matches.add(document[i:j+1])
        
        return matches
    
    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        
        while True:
            children = [key for key in current.keys() if key != self.end_symbol]
            if not children or len(children) > 1:
                break
            
            char = children[0]
            prefix += char
            current = current[char]
        
        return prefix
    
    def advanced_find_matches(self, document, variations):
        matches = set()
        n = len(document)
        
        for i in range(n):
            current_level = self.root
            
            for j in range(i, n):
                char = document[j]
                if char in variations:
                    char = variations[char]  # Replace character if variation exists
                
                if char not in current_level:
                    break
                
                current_level = current_level[char]
                
                if self.end_symbol in current_level:
                    matches.add(document[i:j+1])
        
        return matches
