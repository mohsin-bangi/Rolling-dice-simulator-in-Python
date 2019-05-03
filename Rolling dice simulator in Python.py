import random
import time
user = input("Enter your name:-")
print("Hello",user,"It's time to play rolling dice game!!!!")
for i in range(5):
    print(".")
time.sleep(3)
for i in range(5):
    print(".")

r = random.randint(1,6)
ans = input("ARE YOU READY? Y or N?:-").upper()
if ans == "Y":
    #res = str(r)
    print("result needs to be",r)
    turn = 5
    while turn != 0:
        ans = input("Do you want to throw dice? Y or N").upper()
        if ans == "Y":
            ri = random.randint(1,6)
            print(ri)
            if r == ri:
                print("YOU WON")
                break
            else:
                turn = turn-1
                print("not matched")
                if turn!=0:
                    print("Your remaining turns are =",turn)
                else:
                    print("All chances are over")
                    print("you lose")
                    print("THANK YOU")
        else:
            print("Wrong option selected")
            print("EXIT")
            break
elif ans == "N":
    print("Thank you for visiting")
else:
    print("OOPS! wrong option selected")
    print("EXIT")
    
     
