class Trie:
    def __init__(self, name="root", weight=1):
        self.children = list()
        self.weight = weight
        self.name = name;
        
    def insert(self, path=[], value=1):
        if path:
            child = self.getChild(path[0])
            if child:
                child.weight += value
            else:
                child = Trie(path[0], value)
                self.children.append(child)    
            child.insert(path[1:], value)
            
    def findMinimal(self):
        pass
    
    def printTree(self, indent=0):
        print self.name, self.weight
        for child in self.children:
            print " " * indent, child.printTree(indent + 2)

    def getChild(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return False
        
if __name__ == "__main__":
    trie = Trie()
    urls = ("/Kooperationen/Microsoft/Windows-Server-2015-was-ist-neu", "/Kooperationen/Microsoft/Docker-kooperiert-mit-Microsoft", "/Kooperationen/Microsoft/Windows-Server-2015-was-ist-neu/(tagID)/8")

    for url in urls:
        p = url.split("/")
        trie.insert(p[1:])
    trie.printTree()
