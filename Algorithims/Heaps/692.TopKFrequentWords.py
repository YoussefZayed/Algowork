# Given a non-empty list of words, return the k most frequent elements.

# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
import heapq 
import collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        pairs = collections.defaultdict(int)
        listPairs = []
        for i in words:
            pairs[i] += 1
        for i,j in pairs.items():
            listPairs.append((-j,i))
        
        heapq.heapify(listPairs)
        finalwords = []
        for i in range (k):
            finalwords.append(heapq.heappop(listPairs)[1])
        return finalwords
        