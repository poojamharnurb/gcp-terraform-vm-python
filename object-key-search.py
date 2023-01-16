obj = {'a': {'b': {'c': 'd'}}}
key = 'a'
def print_func(temp, status):
    print("result = ",temp)
    print("status = ",status)

def getfunc(obj, key):
    
    temp = ""
    status = "Not Found"
    if (type(obj)==dict):
        for i in obj :
            if (i == key):
                temp = obj[i]
                print("Value of key is = ",temp)
                status = "Found"
                print_func(temp, status)
                break
            else:
                obj = obj[i]
                getfunc(obj,key)
    else:        
        print_func(temp, status)


getfunc(obj, key) 
