from leetcode_env.environment import LeetCodeEnv
from leetcode_env.types import LeetCodeSubmission, ProgrammingLanguage

import json

slug = "group-anagrams"

code = """
class Solution:
    def groupAnagrams(self, strs: List[str], target):
        
"""


sub = LeetCodeSubmission(code=code,
                         lang=ProgrammingLanguage.PYTHON3,
                         question_slug=slug)

env = LeetCodeEnv()

status, reward, done, submission_result = env.step(sub)

print(status, reward, done)
print(json.dumps(submission_result, indent=4))
