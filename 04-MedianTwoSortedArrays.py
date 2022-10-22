class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        mergedArr = Solution().mergeArrays(nums1, nums2, len(nums1), len(nums2))
        totalLen = len(nums1) + len(nums2)
        if totalLen % 2 == 0:
            return (mergedArr[totalLen // 2] + mergedArr[(totalLen // 2) - 1]) / 2
        return mergedArr[totalLen // 2]

    # Merge sort O(log(n+m))
    def mergeArrays(self, arr1, arr2, n1, n2):
        arr3 = [None] * (n1 + n2)
        i = 0
        j = 0
        k = 0

        while i < n1 and j < n2:
            if arr1[i] < arr2[j]:
                arr3[k] = arr1[i]
                k = k + 1
                i = i + 1
            else:
                arr3[k] = arr2[j]
                k = k + 1
                j = j + 1

        while i < n1:
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1

        while j < n2:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1
        return arr3


print(Solution().findMedianSortedArrays([-7, 1, 4, 8, 22], [-100, 3]))
# arr1 = [1, 4, 5, 6]
# arr2 = [3, 8, 9]
# print(Solution().mergeArrays(arr1, arr2, len(arr1), len(arr2)))
