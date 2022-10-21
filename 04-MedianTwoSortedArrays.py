# TODO
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        medianPos = (len1 + len2) // 2
        pos11 = len1 // 2
        pos12 = len1 // 2
        pos21 = len2 // 2
        pos22 = len2 // 2
        # while True:
        #     if nums1[pos11] < nums2[pos21]:

        return 0


# class Solution:
#     def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
#         medianPos = (len(nums1) + len(nums2)) // 2
#         pos1 = 0
#         pos2 = 0
#         lastItem = 0
#         while True:
#             if (len(nums1) + len(nums2)) % 2 == 0:
#                 if pos1 + pos2 == medianPos:
#                     print("lastitem", lastItem)
#                     if nums1[pos1] < nums2[pos2] and lastItem < nums2[pos2]:
#                         return (nums1[pos1] + lastItem) / 2
#                     if nums1[pos1] < nums2[pos2] and nums2[pos2] < lastItem:
#                         return (nums1[pos1] + nums2[pos2]) / 2
#                     if nums2[pos2] < nums1[pos1] and lastItem < nums1[pos1]:
#                         return (nums2[pos2] + lastItem) / 2
#                     if nums2[pos2] < nums1[pos1] and nums1[pos1] < lastItem:
#                         return (nums1[pos1] + nums2[pos2]) / 2
#
#                 if nums1[pos1] < nums2[pos2]:
#                     if len(nums1) == pos1 + 1:
#                         lastItem = nums2[pos2]
#                         pos2 += 1
#                     else:
#                         lastItem = nums1[pos1]
#                         pos1 += 1
#                 else:
#                     if len(nums2) == pos2 + 1:
#                         lastItem = nums1[pos1]
#                         pos1 += 1
#                     else:
#                         lastItem = nums2[pos2]
#                         pos2 += 1
#                 print("pos", pos1, pos2)
#             else:
#                 if pos1 + pos2 == medianPos:
#                     if nums1[pos1] < nums2[pos2]:
#                         return nums1[pos1]
#                     return nums2[pos2]
#                 if nums1[pos1] < nums2[pos2]:
#                     pos1 += 1
#                 else:
#                     pos2 += 1
#                 print("pos", pos1, pos2)


print(Solution().findMedianSortedArrays([1], [2, 3]))
