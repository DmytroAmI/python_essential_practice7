import random

numbers = [random.randint(1, 100) for i in range(10)]

nums1 = [x ** 5 for x in numbers]
print(type(nums1))
print(nums1)

nums2 = (x ** 5 for x in numbers)
print(type(nums2))
print(nums2)
print(list(nums2))
