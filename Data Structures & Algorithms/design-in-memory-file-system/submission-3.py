class FileSystem:

    def __init__(self):
        self.directories = defaultdict(set)
        self.directories["/"] = set()
        self.files = defaultdict(str)

    def ls(self, path: str) -> List[str]:
        if path in self.files:
            return [path.split('/')[-1]]
        if path in self.directories:
            return sorted(list(self.directories[path]))
        return []

    def mkdir(self, path: str) -> None:
        if path == "/": return
        directories = path.split("/")
        directories.pop(0)
        currPath = "/"
        for directory in directories:
            self.directories[currPath].add(directory)
            if currPath == "/":
                currPath += directory
            else:
                currPath += "/" + directory
            if currPath not in self.directories:
                self.directories[currPath] = set()

    def addContentToFile(self, filePath: str, content: str) -> None:
        self.files[filePath] += content
        before, slash, after = filePath.rpartition('/')
        if not before: before = "/"
        self.directories[before].add(after)

    def readContentFromFile(self, filePath: str) -> str:
        return self.files[filePath]