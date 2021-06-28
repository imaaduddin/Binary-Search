import random

# for i in range(100):
#   numbers.append(random.randint(0, 500))

# print(numbers)

numbers = [27, 459, 50, 357, 160, 459, 32, 461, 425, 378, 412, 103, 471, 13, 266, 208, 445, 142, 3, 123, 67, 19, 280, 479, 253, 331, 26, 420, 236, 28, 214, 133, 406, 217, 138, 322, 408, 489, 427, 496, 330, 418, 303, 484, 94, 321, 122, 80, 426, 482, 162, 170, 3, 260, 23, 213, 178, 93, 309, 159, 353, 37, 195, 7, 381, 358, 151, 196, 107, 193, 176, 494, 441, 118, 228, 44, 395, 407, 23, 202, 366, 474, 128, 176, 392, 434, 203, 488, 5, 171, 1, 107, 54, 407, 438, 193, 132, 488, 73, 68]


numbers.sort()

def binary_search(numbers_list, number, left, right):
  if left > right:
    return -1

  mid = (left + right) // 2
  if number == numbers_list[mid]:
    return mid
  elif number < numbers_list[mid]:
    return binary_search(numbers_list, number, left, mid-1)
  else:
    return binary_search(numbers_list, number, mid+1, right)


