# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

# Define a pair (u,v) which consists of one element from the first array and one element from the second array.

# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        heap = []
        for i in nums1:
            for j in nums2:
                heap.append([i+j,i,j])
        heapq.heapify(heap)
        result = []
        if k > len(heap):
            k = len(heap)
        for _ in range(k):
            result.append(heapq.heappop(heap)[1:])

        return result
        