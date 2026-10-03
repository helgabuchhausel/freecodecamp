class HashTable:
    def __init__(self):
        self.collection = dict

    def hash(self, text):
        return sum(ord(char) for char in text)
    
    def add(self, new_key, new_value):
        return ""
    
    def remove(self, key_to_remove):
        return ""
    
    def lookup(self, key_to_find):
        return None
    

if __name__ == "__main__":
    hash_table = HashTable()

    print(hash_table.hash("text to hash"))

    hash_table.add("test", "test value")




