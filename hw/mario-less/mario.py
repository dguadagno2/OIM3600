height = input("Input a number between 1 and 8 >>")
height = int(height)
print("Height:", height)
if height in range(1, 9) : 
    for i in range (1, height + 1) : 
        for j in range (height - i) :
            print(" ", end = "")
        for n in range (i): 
           print("#", end="") 
        print()
else : 
    print("Please enter a number between 1 and 8")