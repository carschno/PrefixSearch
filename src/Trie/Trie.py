class Trie:
    def __init__(self, name="root", weight=1):
        self.children = list()
        self.weight = weight
        self.name = name;
        
    def insert(self, path=[], value=1):
        """Insert new branch / sub-tree with the given weight (value)."""
        if path:
            child = self.getChild(path[0])
            if child:
                # child with given name (path) found, append
                child.weight += value
            else:
                # no child with given name (path) found, create new branch
                child = Trie(path[0], value)
                self.children.append(child)    
            child.insert(path[1:], value)
            
    def findMinimal(self, minLevel=0, prefix=""):
        """Find the smallest common sub-tree and return the tuple (name, value)."""
        minimals = []
        if minLevel == 0:
            # minimal depth in tree reached
            if len(self.children) == 1:
                # only one child, go down
                map(minimals.append, self.children[0].findMinimal(minLevel, prefix + "/" + self.name))
            else:
                # multiple branches found, attach current node as minimal
                minimals.append((prefix + "/" + self.name, self.weight)) 
        else:
            # go deeper into the tree
            for child in self.children:
                map(minimals.append, child.findMinimal(minLevel - 1, prefix + "/" + self.name))
        return minimals
            
    
    def __str__(self, indent=0):
        """Return a string representation of the tree."""
        output = "  " * indent + "'" + self.name + "' " + str(self.weight) + "\n"
        for child in self.children:
            output += child.__str__(indent + 2)
        return output

    def getChild(self, name):
        """Return the child with the given name or False if there is none."""
        result = False
        for child in self.children:
            if child.name == name:
                # matching child found
                result = child
                break
        return result
        
if __name__ == "__main__":
    trie = Trie()
    urls = ("/Kooperationen/Microsoft/Windows-Server-2015-was-ist-neu", "/Kooperationen/Microsoft/Docker-kooperiert-mit-Microsoft", "/Kooperationen/Microsoft/Windows-Server-2015-was-ist-neu/(tagID)/8", "/Kooperationen/Microsoft/Windows-Server-2015-was-ist-neu/(tagID)/7", "/Kooperationen/Microsoft/Open-Source-in-der-Microsoft-Azure-Cloud", "/Kooperationen/Microsoft/Open-Source-in-der-Microsoft-Azure-Cloud/(tagID)/8")

    for url in urls:
        p = url.split("/")
        trie.insert(p[1:])
    print "Prefix tree:"
    print trie
    
    print "Minimal prefixes:"
    for prefix in trie.findMinimal(3):
        print prefix[0], prefix[1] 
    
    
