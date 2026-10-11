import random
def guess(n):
    random_number=random.randint(1,n)
    user_number=int(input("enter a number:"))
    if user_number>random_number:
        print("number is largest")
    elif user_number<random_number:
        print("number is smallest")
    elif user_number==random_number:
        print("you win")
    else:
        print("")
n=int(input("enter a number:"))
print(guess(n))