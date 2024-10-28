class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
 
            
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for i in range(self.MAX):
            indx =(h+i)%self.MAX
            if len(self.arr[indx])== 0 or self.arr[indx][0] == key:
                self.arr[indx] = (key, val)
                found = True
                break
        if not found:
            raise Exception("Hashmap full")
            
    def __getitem__(self, key):
        found = False
        h = self.get_hash(key)
        for i in range(self.MAX):
            indx = (h+i)%self.MAX
            kv = self.arr[indx]
            if kv == []:
                break
            if kv[0]== key:
                found = True
                return kv[1]
                break
        if not found:
            raise Exception("Key not found")
            
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        found = False
        for i in range(self.MAX):
            indx = (h+i)%self.MAX
            kv = self.arr[indx]
            if kv == []:
                break
            if kv[0]== key:
                print("del",kv[0])
                del self.arr[indx]
                found = True
                break
        if not found:
            raise Exception("Key not found")

if __name__ == "__main__":
    t = HashTable()
    t["march 6"] = 310
    t["march 7"] = 420
    t["march 8"] = 67
    t["march 17"] = 63457
    t["march 9"] = 31
    t["march 10"] = 310
    t["march 11"] = 420
    t["march 12"] = 67
    t["march 13"] = 63457
    
    print(t.arr)
    print(t.arr)
    d ={}
    print(dir(d))