def print_f(num):
    print("The factors of the  ",num,"are:")
    for i in range(1, num+1):
        if num % i == 0 :
            print(i)
num = int(input("enter your number"))
print_f(num)