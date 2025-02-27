
"""
Basic Practice on `*args` and `**kwargs`
✔ *args → Collects multiple positional arguments as a tuple.
✔ **kwargs → Collects multiple named arguments as a dictionary.
✔ They can be used together for flexible function definitions.

Feature	*args	**kwargs
Input Type	Positional arguments	Keyword (named) arguments
Output Type	Tuple	Dictionary
Use Case	Pass multiple values	Pass multiple named values
Example Call	func(1, 2, 3)	func(name="Alice", age=25)

"""
class UserMainCode(object):
    #Loading constructor default values
    def __init__(self,**kwargs):
        self.name = kwargs.get("Name","Unknown")
        self.age = kwargs.get("Age",0)

    def show(self):
        print(f"User Name : {self.name} , Age : {self.age}")

    def show_with_kwargs(self,**kwargs):
        print(f"User Name : {kwargs["Name"]}, Age : {kwargs["Age"]}")

    @classmethod
    def print_my_result(cls, **args) -> None:
        print("Nothing...")
        print(f"{args}")


class Decorator_practice(object):

    # Loading Default Constructor values
    def __init__(self , **kwargs):
        self.num1 = kwargs.get("Num1",2)
        self.num2 = kwargs.get("Num2",3)

    def sum_numbers(self, *args):
        print(sum(args))


class Master(object):

    def my_decorator(self,func):
        def wrapper():
            print("Log Before Func Call . . . ")
            func()
            print("Log After Func Call . . . ")
        return wrapper

    @staticmethod
    def greet(name = "Surya"):
        print(f"Hi ! {name}")
        # self.name = kwargs["name"]
        # print(f"Hello ! {kwargs}")


# Driver Call
if __name__=="__main__" :

    # Object Creation for User Main Code Class
    obj = UserMainCode(Name = "Surya",Age = "25")
    obj.print_my_result(Msg = "Hello")

    # Calling method contains keyword arguments -> return dictonary output where as args returns tuple output.
    obj.show()   # Show original object details

    # Calling method with kwargs items
    obj.show_with_kwargs(Name="Ruchitha",Age="24")  # Show details with new kwargs, but do not modify original object values

    # Verify that the original values are not changed
    obj.show()

    # Creating Decorator practice class object
    dec_obj = Decorator_practice()

    # Returning args sum value by func call
    dec_obj.sum_numbers(1,2,3,4,5,6,7,8)

    # Pointing to default number refering to constructor defines value
    print(dec_obj.num2)

    # Decorator behaviour understanding
    obj_master = Master()

    # Decorating the function explicitly
    #obj_master.name = "Hari"
    decorated_greet = obj_master.my_decorator(obj_master.greet)

    # Calling the decorated function
    decorated_greet()