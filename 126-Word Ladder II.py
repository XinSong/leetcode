
from queue import Queue
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        q = Queue()
        q.put([beginWord,[beginWord]])
        min_path = float('inf')
        path_memory = dict()
        path_memory[beginWord] = [beginWord]
        res = []
        while not q.empty():
            word, word_path = q.get()
            if len(word_path) > min_path:
                break
            if word == endWord:
                res.append(word_path)
                min_path = len(word_path)
            else:
                for __word in wordList:
                    if self.isValidLadder(word, word_path, __word):
                        __word_path = word_path + [__word]
                        if __word not in path_memory:
                            path_memory[__word] = __word_path
                            q.put([__word, word_path + [__word]])
                        elif len(path_memory[__word]) == len(__word_path):
                            q.put([__word, word_path + [__word]])
        return res

    def isValidLadder(self, word, word_path, ladder_word):
        if ladder_word in word_path:
            return False
        distance = 0
        for idx in range(0, len(word)):
            if word[idx] != ladder_word[idx]:
                distance += 1
                if distance > 1:
                    return False
        if distance == 1:
            return True
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(solution.findLadders(beginWord, endWord, wordList))
"""
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        res = []
        shortest = float('inf')
        ladder = [-1] * len(wordList)
        layer = 0
        curWord = beginWord

        if endWord not in wordList:
            return res

        while 0<= layer < len(wordList):
            ladder[layer] += 1
            while ladder[layer] < len(wordList) and not self.isValidLadder(curWord, wordList, ladder, layer):
                ladder[layer] += 1
            if ladder[layer] != len(wordList):
                if wordList[ladder[layer]] == endWord: 
                    __res = [beginWord]
                    for __layer_idx in range(0,layer):
                        __res.append(wordList[ladder[__layer_idx]])
                    __res.append(endWord)
                    if layer < shortest:
                        res = []
                        shortest = layer
                    res.append(__res)
                    ladder[layer] = -1
                    layer -= 1
                    if layer == 0:
                        curWord = beginWord
                    else:
                        curWord = wordList[ladder[layer-1]]
                elif layer+1<=shortest and self.isValidLadder(endWord, wordList, ladder, layer):
                    __res = [beginWord]
                    for __layer_idx in range(0,layer):
                        __res.append(wordList[ladder[__layer_idx]])
                    __res.append(wordList[ladder[layer]])
                    __res.append(endWord)
                    if layer+1 < shortest:
                        res = []
                        shortest = layer + 1
                    res.append(__res)
                else:
                    if layer < shortest:
                        curWord = wordList[ladder[layer]]
                        layer += 1

            else:
                ladder[layer] = -1       
                layer -= 1
                if layer == 0:
                    curWord = beginWord
                else:
                    curWord = wordList[ladder[layer-1]]
        return res
    
    def isValidLadder(self, word, wordList, ladder, layer):
        if ladder[layer] in ladder[0:layer]:
            return False
        distance = 0
        for idx in range(0, len(word)):
            if word[idx] != wordList[ladder[layer]][idx]:
                distance += 1
                if distance > 1:
                    return False
        if distance == 1:
            return True
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(solution.findLadders(beginWord, endWord, wordList))
"""