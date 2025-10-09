class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts1 = Counter(nums1)
        counts2 = Counter(nums2)
        intersection_counter = counts1 & counts2

        # Return the elements based on the intersection counts
        return list(intersection_counter.elements())