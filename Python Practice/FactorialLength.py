# Sample Logic 

# def fact(n): return [1 if n==0 or n==1 else n*fact(n-1)][0]
# def getLenthOfFact(x:int) -> int: print(len(str(x)))

class Solution(object):
    @decorator
    def findLengthOfFact(factorial) -> int:
        def wrapper():
            print("Before Factorial") #Sample LOG Logic implements here
            factorial(5)
            print("After Factorial") #Sample LOG Logic implements here
        return wrapper


if "__name__"=="__main__":
    obj = Solution()
    x = 5#int(input())
    obj.findLengthOfFact(factorial(x))
