# Python 2.7

# Given an array of integers,
# return indices of the two numbers such that
# they add up to a specific target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# nums = [2, 7, 11, 15]
# target_number = 9
#
#
# def consecutive_two_sum(number, target):
#     array_two_sum = []
#
#     for index, num in enumerate(number):
#         print(index, num)
#         for index2, num2 in enumerate(number[1:]):
#             print(index2, num2)
#             goal = num + num2
#             print(goal)
#             array_two_sum.append(index)
#             array_two_sum.append((index2 + 1))
#             if goal is target:
#                 print('met')
#                 array_two_sum.append(index)
#                 array_two_sum.append((index2 + 1))
#             else:
#                 print('not met')
#                 goal = 0
#
#     return array_two_sum
#
# print('This is the answer:')
# print(consecutive_two_sum(nums, target_number))


nums = [2, 7, 11, 15]
target_number = 9

def any_two_sum(number, target):
    array_two_sum = []

    for index, num in enumerate(number):
        print(index, num)
        for index2, num2 in enumerate(number[1:]):
            print(index2, num2)
            goal = num + num2
            print(goal)
            if goal is target:
                print('met')
                array_two_sum.append(index)
                array_two_sum.append((index2 + 1))
            else:
                print('not met')
                goal = 0

    return array_two_sum

print('This is the answer:')
print(any_two_sum(nums, target_number))
