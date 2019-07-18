
name = input("What is your name?\n")
favorite = input("What is your favorite food?\n")

def isGoodTaste(name, favorite):
    return "Hello " + name + " you have great taste in food. My favorite food is also " + favorite + "."
    
print(isGoodTaste(name, favorite))
    