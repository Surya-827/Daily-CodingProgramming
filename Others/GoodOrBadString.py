class Solution:
    def isGoodorBad(self, S):
        v = "aeiou"
        def isV(p):
            return all([(x in v or x is "?") for x in p])
        def isC(p):
            return all([(x not in v or x is "?") for x in p])
        j = 0
        n = len(S)

        while j < n:
            # check for a bad substring
            if (j + 5 < n and isV(S[j:j + 6])) or (j + 3 < n and isC(S[j:j + 4])):
                return 0
            else:
                j += 1
        return 1

if __name__=="__main__":
    s = input()
    obj = Solution()
    result = obj.isGoodorBad(s)
    print(result)