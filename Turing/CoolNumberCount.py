

class Solution(object):
    @classmethod
    def getCoolNumberCount(cls,s:str) -> int:
        coolNumberLength = 4
        count=0
        for i in range(len(s)-coolNumberLength+1):
            sub_str = s[i:i+coolNumberLength]

            if len(set(sub_str))==coolNumberLength:
                count+=1
        return count



if __name__=="__main__":

    sol = Solution()
    s = input()
    print(sol.getCoolNumberCount(s))