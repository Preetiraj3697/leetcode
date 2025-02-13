# You are given a 0-indexed array of unique strings words.
#
# A palindrome pair is a pair of integers (i, j) such that:
#
#
# 	0 <= i, j < word.length,
# 	i != j, and
# 	words[i] + words[j] (the concatenation of the two strings) is a palindrome.
#
#
# Return an array of all the palindrome pairs of words.
#
#  
# Example 1:
#
#
# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
#
#
# Example 2:
#
#
# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]
#
#
# Example 3:
#
#
# Input: words = ["a",""]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["a","a"]
#
#
#  
# Constraints:
#
#
# 	1 <= words.length <= 5000
# 	0 <= words[i].length <= 300
# 	words[i] consists of lowercase English letters.
#
#


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # keep a hashmap of word to its index
        idx_map = {}
        for i, word in enumerate(words):
            idx_map[word] = i
            
        res = set()
        for i, word in enumerate(words):
            if not word:
                # we don't process empty string by itself
                continue
            
            # generate all possible LHS that would form
            # a palindrome with current word
            for j in range(len(word)):
                current = word[:j]
                target = word[j:][::-1]
                if current == current[::-1] and target != word and target in idx_map:
                    res.add((idx_map[target], i))
                    
            # generate all possible RHS that would form
            # a palindrome with current word
            for j in range(len(word), -1, -1):
                current = word[j:]
                target = word[:j][::-1]
                if current == current[::-1] and target != word and target in idx_map:
                    res.add((i, idx_map[target]))
                    
            # check if current word is already a palindrome and
            # if we have an empty string in our map
            if word == word[::-1] and "" in idx_map:
                idx = idx_map[""]
                res.add((i, idx))
                res.add((idx, i))

        return list(res)
    
