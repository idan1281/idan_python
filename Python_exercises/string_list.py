string = input("please enter a string: ")
wrd = str(string)
rvs = wrd[::-1]
if wrd == rvs:
    print("this string is a palindrome")
else:
    print("this is NOT a paliaandrome")