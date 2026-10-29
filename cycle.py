import time

def cycle_print(variable,time1):
    for i in variable:
        print(i)
        time.sleep(time1)

def prefix_add(variable,*items):
    return variable + list(items)

def prefix_remove(variable,item):
    variable.remove(item)
    return variable
