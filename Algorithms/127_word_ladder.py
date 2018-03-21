class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if beginWord == endWord:
            return 1
        dict = set(wordList)
        queue = collections.deque([beginWord])
        length = 0
        wordLen = len(beginWord)
        while queue:
            length += 1
            n = len(queue)
            for i in xrange(n):
                word = queue.popleft()
                if word == endWord:
                    return length
                for j in xrange(wordLen):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c != word[j]:
                            nextWord = word[:j] + c + word[j+1:]
                            if nextWord in dict:
                                queue.append(nextWord)
                                dict.remove(nextWord)

        return 0
