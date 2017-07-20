num = int(input("please enter a number: "))
mod = num % 2

if num % 4 == 0:
    print("the number ",num, " is a miltiple of 4")
elif num % 2 == 0:
    print("the number",num,"is even")

else:
    print("the number",num, "is an odd number")