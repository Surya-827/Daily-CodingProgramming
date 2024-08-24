
s = "PROGRAM"

def getPattern(s):
    n=len(s)
    mid = n//2
    for i in range(n+1,-1 ,-1):
        left=mid-i
        right=mid+i+1
        print(s[left:right])
    print()


getPattern(s)

"""
Late binding
"""
def my_funcs(n):
    return [lambda  x : x*i for i in range(n)]

fun=my_funcs(9)
print([f(5) for f in fun])
print("\u003B")