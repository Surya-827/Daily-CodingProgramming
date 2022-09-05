from typing import List

class Solution(object):
    @classmethod
    def rotate(cls,N:int,D:int) -> List[int]:
        out = [0]*2
        D = D % 16
        binNum = bin(N)[2:]
        binNum = "{:>016}".format(binNum)
        out[0],out[1] = int(binNum[D:]+binNum[:D],2), int(binNum[-D:]+binNum[:-D],2)
        return out


if __name__=="__main__":
    N,D = map(int,input().split())
    obj = Solution()
    result = obj.rotate(N,D)
    for i in result:
        print(i)

