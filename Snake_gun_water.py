import random
def gamewin(comp ,you):
    if comp == you:
        return None
    elif comp == 's':
        if you =='w':
            return False
        elif you =='g':
            return True          
    elif comp == 'w':
        if you =='g':
            return False
        elif you =='s':
            return True
    elif comp == 'g':
        if you =='s':
            return False
        elif you =='w':
            return True

print("comp turn : snake(s), water(w) and gun(g)")
radNo = random.randint(1,3)
if radNo ==1 :
    comp = 's'
elif radNo==2:
    comp = 'w'
elif radNo ==3:
    comp = 'g'

you = input(" your turn : snake(s), water(w) and gun(g) )(choose any one)= ") 
a = gamewin(comp, you)
print (f" option selected by computer is {comp}")
print (f" option selected by  you is {you}")

if a == None:
    print("tie ")
elif a == True:
    print("you win. ")
else :
    print("you loose.")
 
