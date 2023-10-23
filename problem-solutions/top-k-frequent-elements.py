from leetcode_env.environment import LeetCodeEnv
from leetcode_env.types import LeetCodeSubmission, ProgrammingLanguage

slug="top-k-frequent-elements"

code = """
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # map num : occurence 
        freq = [[] for i in range(len(nums) + 1)] # each cell is # of occurence, and each cell stores the n that has that many occurence
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for key, value in count.items():
            freq[value].append(key)

        # loop from end to beginning
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if (len(res) == k):
                    return res

        return
"""

sub = LeetCodeSubmission(code=code,
                         lang=ProgrammingLanguage.PYTHON3,
                         question_slug=slug)

env = LeetCodeEnv()

status, reward, done, submission_result = env.step(sub)

print(status, reward, done, submission_result)

