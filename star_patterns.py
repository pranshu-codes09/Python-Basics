# For right angle triangle 
for i in range (0,5):
    print("*"*i)


# For triangle
n = 5
for i in range (1,5):
    print(" "*(n-i)+"*"*(2*i-1))



# For box pattern
n = 5
for i in range (1,6):
    if i == 1 or i == n:
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")


# For diamond pattern
n = 4
print(" "*(n-i)+"*")

#For upper
for i in range (1,5):
    print(" "*(n-i)+"*"+" "*(2*i-1)+"*")

#For lower
for i in range (3,0,-1):
    print(" "*(n-i)+"*"+" "*(2*i-1)+"*")
print(" "*(n-i)+"*")



