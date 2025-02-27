import time as t

class UserMainCode(object):

    def timing_decorator(func):
        def wrapper(*args,**kwargs):
            start_time = t.time()
            result = func(*args,**kwargs)
            end_time = t.time()
            print(f"{func.__name__} is executed in {end_time - start_time : .4f} seconds")
            return result
        return wrapper

    @timing_decorator
    def get_log_details(self):
        t.sleep(2)
        print("Function is Executed")


if __name__=="__main__":
    obj = UserMainCode()
    obj.get_log_details()