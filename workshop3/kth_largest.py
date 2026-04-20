import heapq

def kth_largest(nums, k):
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]

nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
print(kth_largest(nums1, k1))

nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4
print(kth_largest(nums2, k2))
