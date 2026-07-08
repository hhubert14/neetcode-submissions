class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        ans = set()
        seen = set()

        def dfs(row, col, node, currWord):
            if node.isWord:
                ans.add(currWord)
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return
            if board[row][col] not in node.children:
                return
            if (row, col) in seen:
                return
            seen.add((row, col))
            dfs(row+1,col,node.children[board[row][col]],currWord + board[row][col])
            dfs(row-1,col,node.children[board[row][col]],currWord + board[row][col])
            dfs(row,col+1,node.children[board[row][col]],currWord + board[row][col])
            dfs(row,col-1,node.children[board[row][col]],currWord + board[row][col])
            seen.remove((row,col))
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row,col,root,"")
        return list(ans)

