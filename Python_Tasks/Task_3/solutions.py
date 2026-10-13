"""solutions.py - Task 3: Python Coding & Problem-Solving (15 functions)"""


# Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    freq = {}
    for word in sentence.split():
        freq[word] = freq.get(word, 0) + 1
    return freq


# Q2. Find the Frequency of Each Character in a Word
def char_frequency(word):
    freq = {}
    for ch in word:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


# Q3. Find the First Non-Repeating Character in a Word
def first_non_repeating(word):
    freq = char_frequency(word)
    for ch in word:
        if freq[ch] == 1:
            return ch
    return None


# Q4. Check Whether Two Strings Are Anagrams
def are_anagrams(s1, s2):
    return char_frequency(s1) == char_frequency(s2)


# Q5. Find the First Repeating Character in a String
def first_repeating(text):
    seen = set()
    for ch in text:
        if ch in seen:
            return ch
        seen.add(ch)
    return None


# Q6. Move All Zeros to the End of a List
def move_zeros_to_end(nums):
    non_zeros = [n for n in nums if n != 0]
    zero_count = len(nums) - len(non_zeros)
    return non_zeros + [0] * zero_count


# Q7. Find the Second Highest Distinct Number in a List
def second_highest(nums):
    distinct = sorted(set(nums), reverse=True)
    if len(distinct) < 2:
        return None
    return distinct[1]


# Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates(nums):
    seen = set()
    result = []
    for n in nums:
        if n not in seen:
            seen.add(n)
            result.append(n)
    return result


# Q9. Find the Missing Number from 1 to N
def missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)


# Q10. Find Two Numbers Whose Sum Equals a Target
def two_sum_pair(nums, target):
    seen = set()
    for num in nums:  # 'num' is the second element of the pair
        complement = target - num
        if complement in seen:
            return [complement, num]
        seen.add(num)
    return []


# Q11. Find the Number Closest to Zero
def closest_to_zero(nums):
    if not nums:
        return None
    # smallest distance first; on a tie, the larger (positive) value wins
    return min(nums, key=lambda x: (abs(x), -x))


# Q12. Find Common Elements Between Two Lists
def common_elements(list1, list2):
    set2 = set(list2)
    added = set()
    result = []
    for item in list1:
        if item in set2 and item not in added:
            result.append(item)
            added.add(item)
    return result


# Q13. Rotate a List to the Right by K Positions
def rotate_right(nums, k):
    if not nums:
        return []
    k = k % len(nums)
    if k == 0:
        return nums[:]
    return nums[-k:] + nums[:-k]


# Q14. Find the Maximum Sum of Two Consecutive Elements
def max_consecutive_sum(nums):
    best = nums[0] + nums[1]
    for i in range(1, len(nums) - 1):
        best = max(best, nums[i] + nums[i + 1])
    return best


# Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def all_pairs_with_sum(nums, target):
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1

    pairs = []
    for a in counts:
        b = target - a
        if a < b and b in counts:
            pairs.append([a, b])
        elif a == b and counts[a] >= 2:  # needs two distinct positions
            pairs.append([a, b])
    pairs.sort(key=lambda p: p[0])
    return pairs