import random
print("Welcome to the Snake,Water,Gun game.")
def gameWin (comp,you):
    if comp==you:
        return None
    elif comp=="s":
        if you=="w":
             return False
            
        elif you=="g":
             return True
            
              
    elif comp=="w":
        if you=="s":
            return True
        elif you=="g":
            return False
    elif comp=="g":

        if you=="w":
            return True
        elif you=="s":
            return False            

       
    

print("Comp turn:snake{s},water{w},gun{g}:")

r=random.randint(1,3)

if r==1:
    comp="s"
elif r==2:
    comp="w"
else:
    comp="g"



you=input("Your turn:snake{s},water{w},gun{g}:")
print("Comp chose:",comp)
print("You chose:",you)

a=gameWin(comp,you)
if a==None:
    print("Game is tie!")
elif a:
    print("You won")
else:
    print("You lost!")             





     




