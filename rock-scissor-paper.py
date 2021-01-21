import random
run=True
uscore=0
cscore=0

def display():
    print("1. Rock")
    print("2. Scissor")
    print("3. Paper")
    print("4. Quit\n")

while run :
    display()
    choice=int(input("Enter your choice :\n"))
    n=random.randint(1,4)

    

    if choice==1:
        if n==1:
            print("Your Choice : Rock")
            print("Comp Choice : Rock")
            print("Match tied ...!\n")
           
        elif n==2:
            print("Your Choice : Rock")
            print("Comp Choice : Scissor")
            print(" You Win...!\nCongratulation...!\n")
            uscore+=1
        elif n==3:
            print("Your Choice : Rock")
            print("Comp Choice : Paper")
            print("Opps..\nYou lose...!\n")
            cscore+=1
        print("Play again \n")
        print("Your score : ",uscore)
        print("Computer score : ",cscore)
        print("")

    elif choice==2:
        print("Your Choice : Scissor")
        if n==1:
            
            print("Comp Choice : Scissor")
            print("Match tied ...!\n")
           
        elif n==2:
            print("Comp Choice : Rock")
            print(" You Win...!\nCongratulation...!\n")
            cscore+=1
        if n==3:
            print("Comp Choice : Paper")
            print("Opps..\nYou lose...!\n")
            uscore+=1
        print("Play again \n")
        print("Your score : ",uscore)
        print("Computer score : ",cscore)
        print("")

    elif choice==3:
        print("Your Choice : Paper")

        if n==1:
            print("Comp Choice : Paper")
            print("Match tied ...!\n")
           
        elif n==2:
            print("Comp Choice : Rock")
            print(" You Win...!\nCongratulation...!\n")
            uscore+=1
           
        elif n==3:
            print("Comp Choice : Scissor")
            print("Opps..\nYou lose...!\n")
            cscore+=1
        
        print("Play again \n")
        print("Your score : ",uscore)
        print("Computer score : ",cscore)
        print("")
            
    elif choice==4:
        print("Your Score Board :\n")
        if uscore > cscore:
            print("Your score : ",uscore)
            print("comp score : ",cscore)
            print("Congratulation...!\nYou win !\n")
        elif uscore< cscore:
            print("Your score : ",uscore)
            print("comp score : ",cscore)  
            print("Opps..! \nYou Lose  !\n")
        else:
            print("Match tied")  

        run=False        


    else:
        print("Invalid code ")

