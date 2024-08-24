

class Solution(object):
    @classmethod
    def breakTheBricks(cls,bigHits, newtons):
        n = len(newtons)
        indexed_newtons = sorted(enumerate(newtons), key=lambda x: x[1])

        total_hits = 0
        big_hammer_hits = []
        small_hammer_hits = []

        for i in range(min(bigHits, n)):
            index, force = indexed_newtons[n - 1 - i]
            big_hammer_hits.append(index + 1)
            total_hits += 1


        for i in range(n - len(big_hammer_hits)):
            index, force = indexed_newtons[i]
            small_hammer_hits.append(index + 1)
            total_hits += force

        if not big_hammer_hits:
            big_hammer_hits = [-1]

        if not small_hammer_hits:
            small_hammer_hits = [-1]

        return [[total_hits], sorted(big_hammer_hits), sorted(small_hammer_hits)]
   
    # Example usage
    # bigHits = 4
    # newtons = [3, 2, 5, 4, 6, 7, 9]



if __name__=="__main__":
    Sol = Solution()
    bigHits = int(input())
    newtons = list()
    for _ in range(int(input())):
        newtons.append(int(input()))
    result = Sol.breakTheBricks(bigHits,newtons)

    for i in result:
        if(type(i)==list):
            print(*i)

