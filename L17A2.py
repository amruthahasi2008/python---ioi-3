num_s = int(input("enter the smallest number"))
num_l = int(input("enter the largest number"))
while num_s :
    num_store = num_s
    num_s = num_l % num_s
    num_l = num_store

print("hcf is",num_l)