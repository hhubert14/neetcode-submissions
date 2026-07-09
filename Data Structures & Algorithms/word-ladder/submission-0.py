class ListNode:
    def __init__(self, string):
        self.string = string
        self.next = []

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def canTransform(word1, word2):
            diff_count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:  # Compare characters, not ASCII values
                    diff_count += 1
            return diff_count == 1

        wordList.append(beginWord)
        if endWord not in wordList:
            return 0

        nodes = {}
        for word1 in wordList:
            for word2 in wordList:
                if word1 == word2:
                    continue
                if word1 not in nodes:
                    nodes[word1] = ListNode(word1)
                if word2 not in nodes:
                    nodes[word2] = ListNode(word2)
                if abs(canTransform(word1, word2)):
                    nodes[word1].next.append(nodes[word2])
                    nodes[word2].next.append(nodes[word1])
        print(nodes)
        for node in nodes.values():
            print(node.string)
            print(node.next)
        queue = deque()
        queue.append(nodes[beginWord])
        currLen = 1
        seen = set()
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.string == endWord:
                    return currLen
                if node in seen:
                    continue
                seen.add(node)
                for nextNode in node.next:
                    queue.append(nextNode)
            currLen += 1
        return 0



        
