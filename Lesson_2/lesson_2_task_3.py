import math
def square(side):
    result=side*side
    if result==int(result):
        return result
    else: return math.ceil(result) 

x=square(3.5)
print(x)
