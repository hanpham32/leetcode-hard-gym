from leetcode_env.environment import LeetCodeEnv
from leetcode_env.types import LeetCodeSubmission, ProgrammingLanguage
import json

slug="two-sum"

code = """
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if (diff in hashmap):
                return [hashmap[diff], i]
            else:
                hashmap[n] = i
        
        return False
"""

"""
Notes:
(O)n solution
- use a dictionary to store the diff to index
- retrieve and return if found -> (O)n linear solution

        # brute force solution
        # l = len(nums)
        # for i in range(l - 1):
            # for j in range(i + 1, l):
                # if nums[i] + nums[j] == target:
                    # return [i, j]
"""

sub = LeetCodeSubmission(code=code,
                         lang=ProgrammingLanguage.PYTHON3,
                         question_slug=slug)

env = LeetCodeEnv()

status, reward, done, submission_result = env.step(sub)


print(status, reward, done)
print(json.dumps(submission_result, indent=4))

