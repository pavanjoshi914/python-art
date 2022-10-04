a = int(input("enter number to creat table = "))
table = [a*i for i in range(1,11) ]
print(str(table) )
with open("table.text","w")as f:
    f.write(str(table))


# infinate or valid question ............

c = int(input("enter neumirator = "))
d = int(input("enter denominator = "))
try:
    e = c/d
    if c  > 0:
        print("no problem in question")
    else :
        print("do not make 0 in neumirator , it is from not defined34") 
    print(e)       
except:
    print("infinate")
