class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.eow=False
class Trie:
    def __init__(self):
        self.root=self.getnode()
    def getnode(self):
        return TrieNode()
    def insertstring(self,string):
        currnode=self.root
        length=len(string)
        for level in range(length):
            i=ord(string[level])-ord('a')
            if not currnode.children[i]:
                currnode.children[i]=self.getnode()
            currnode=currnode.children[i]
        currnode.eow=True
    def searchstring(self,string):
        currnode=self.root
        n=len(string)
        for j in range(n):
            i=ord(string[j])-ord('a')
            if not currnode.children[i]:
                return False
            currnode=currnode.children[i]
        return True
        

keys=["apple","app","the","there","hello","surbhi"]
n=len(keys)
t=Trie()
for key in keys:
    t.insertstring(key)
print(t.searchstring("hello"))
