# package


"""
Class

method
vartables

loops
logic

main fubc() call

"""

# Write a program which do all arthimetic and logical operations !
import pyttsx3 as p

class Operators:
    @classmethod
    def ArthimeticFunction(cls,x,y,z):
        if(z=="+"):
            return f"{x} {z} {y} = {x+y}"
        elif(z=="-"):
            return f"{x} {z} {y} = {x-y}"
        elif(z=="*"):
            return f"{x} {z} {y} = {x*y}"
        elif(z=="/" or z=="//"):
            return f"{x} {z} {y} = {x//y}"
        elif(z=="%"):
            return f"{x} {z} {y} = {x%y}"
        else:
            return -1

    @classmethod
    def BitwiseFunction(cls,x,y,z):
        if(z== "&"):
            return f"{x} {z} {y} = {x&y}"
        if(z == "|"):
            return f"{x} {z} {y} = {x|y}"
        if(z == "^"):
            return f"{x} {z} {y} = {x ^ y}"
        if(z == "!"):
            return f"{x} {z} {y} = {x != y}"
        if(z == "="):
            return f"{x} {z} {y} = {x == y}"




#Rule -> BODMAS Bracket of division multiplication addition substraction

if __name__=="__main__":
    charan = Operators()
    x=3
    y=2
    z="/"
    k="^"

    buddy = p.init()
    print(charan.ArthimeticFunction(x,y,z))
    buddy.say(f"Hey Charan ! your arthmetic function values says {charan.ArthimeticFunction(x,y,z)}")
    print(charan.BitwiseFunction(x,y,k))
    buddy.say(f"Hey Charan ! your bitwise function values says {charan.BitwiseFunction(x,y,k)}")
    buddy.runAndWait()

