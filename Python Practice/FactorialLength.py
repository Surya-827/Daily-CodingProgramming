# Sample Logic 

def fact(n):
    return *[if n==0 or n==1:return 1 else n*fact(n-1)]


print(fact(5))
