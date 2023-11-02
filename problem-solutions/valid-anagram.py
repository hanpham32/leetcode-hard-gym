from leetcode_env.environment import LeetCodeEnv
from leetcode_env.types import LeetCodeSubmission, ProgrammingLanguage

slug="valid-anagram"

code = """
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check for base case
        if (len(s) != len(t)):
            return False

        # create two dictionary
        countS, countT = {}, {}
        
        # loop & count characters
        for i in range (len(s)):
            countS[s[i]] = 1 + countS[s[i], 0]
            countT[t[i]] = 1 + countT[t[i], 0]

        # loop countS & check quantity of characters
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
"""

sub = LeetCodeSubmission(code=code,
                         lang=ProgrammingLanguage.PYTHON3,
                         question_slug=slug)

env = LeetCodeEnv()

status, reward, done, submission_result = env.step(sub)

print(status, reward, done, submission_result)

