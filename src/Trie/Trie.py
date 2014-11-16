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
    
    def __str__(self, indent=0):
        output = " " * indent + self.name + " " + str(self.weight) + "\n"
        for child in self.children:
            output += child.__str__(indent + 2)
        return output

    def getChild(self, name):
        result = False
        for child in self.children:
            if child.name == name:
                result = child
                break
        return result
        
if __name__ == "__main__":
    trie = Trie()
    urls = ("/Kooperationen/Microsoft/Windows-Server-2015-was-ist-neu", "/Kooperationen/Microsoft/Docker-kooperiert-mit-Microsoft", "/Kooperationen/Microsoft/Windows-Server-2015-was-ist-neu/(tagID)/8")

    for url in urls:
        p = url.split("/")
        trie.insert(p[1:])
    print trie.__str__()
