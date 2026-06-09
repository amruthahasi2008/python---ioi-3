num = int(input("enter your number"))
orginal_num = num
rev = 0
while num >0 :
    digit = num %10
    rev = rev *10 +digit
    num = num //10

if orginal_num == rev :
    print(f"{orginal_num} is a palindrome number")
else :
    print(f"{orginal_num} is not a palindrome number")

