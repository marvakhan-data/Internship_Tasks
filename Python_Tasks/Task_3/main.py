"""main.py - imports all 15 functions and tests each one."""
from solutions import (
    word_frequency, char_frequency, first_non_repeating, are_anagrams,
    first_repeating, move_zeros_to_end, second_highest, remove_duplicates,
    missing_number, two_sum_pair, closest_to_zero, common_elements,
    rotate_right, max_consecutive_sum, all_pairs_with_sum,
)

print("Q1:", word_frequency("python is easy and python is powerful"))
print("Q1 (additional_test_case):", word_frequency("to be or not to be"))

print("Q2:", char_frequency("banana"))
print("Q2 (additional_test_case):", char_frequency("hello"))

print("Q3:", first_non_repeating("swiss"))
print("Q3 (additional_test_case):", first_non_repeating("aabb"))

print("Q4:", are_anagrams("listen", "silent"))
print("Q4 (additional_test_case):", are_anagrams("hello", "world"))

print("Q5:", first_repeating("programming"))
print("Q5 (additional_test_case):", first_repeating("abc"))

print("Q6:", move_zeros_to_end([0, 3, 0, 1, 2, 0, 4]))
print("Q6 (additional_test_case):", move_zeros_to_end([0, 0, 5, 0, 9]))

print("Q7:", second_highest([10, 20, 40, 30, 40, 20]))
print("Q7 (additional_test_case):", second_highest([5, 5, 5]))

print("Q8:", remove_duplicates([4, 2, 4, 5, 2, 7, 5]))
print("Q8 (additional_test_case):", remove_duplicates([1, 1, 1, 2, 3, 3]))

print("Q9:", missing_number([1, 2, 4, 5, 6], 6))
print("Q9 (additional_test_case):", missing_number([2, 3, 1, 5], 5))

print("Q10:", two_sum_pair([2, 7, 11, 15], 9))
print("Q10 (additional_test_case):", two_sum_pair([1, 2, 3], 10))

print("Q11:", closest_to_zero([-8, -3, 2, 5, -2]))
print("Q11 (additional_test_case):", closest_to_zero([-4, 4, 7]))

print("Q12:", common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print("Q12 (additional_test_case):", common_elements([1, 2, 2, 3], [2, 3, 3]))

print("Q13:", rotate_right([1, 2, 3, 4, 5], 2))
print("Q13 (additional_test_case):", rotate_right([1, 2, 3], 4))

print("Q14:", max_consecutive_sum([4, 7, 2, 9, 5]))
print("Q14 (additional_test_case):", max_consecutive_sum([-1, -5, -2]))

print("Q15:", all_pairs_with_sum([2, 4, 3, 5, 7, 8, 1], 9))
print("Q15 (additional_test_case):", all_pairs_with_sum([3, 3, 3, 6], 6))