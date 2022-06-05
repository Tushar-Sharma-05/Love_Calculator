import math

def cans(height,width):
    no_of_cans = math.ceil((height*width)/coverage)
    return no_of_cans
    
height = int(input("Enter The Height Of The Wall:"))
width = int(input("Enter The Width Of The Wall:"))
coverage = 5
print(f"The total no of cans required are:",cans(height,width))