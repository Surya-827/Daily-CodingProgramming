

class Practice(object):
    @staticmethod
    def createDictionary(*args) -> dict:
        d = {}
        for key,value in args:
            d[key] = value
        return d

    @staticmethod
    def createDict(**kwargs) -> dict:
        return kwargs

if __name__=="__main__":
    obj = Practice()
    print(obj.createDictionary(('Surya','LTI'),('Sudha','Synergy')))
    print(obj.createDict(Name="Surya",Company="LTI"))