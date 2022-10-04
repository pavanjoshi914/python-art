def sum_recursion(n):
    if n == 0:
        return 0
    return n + (sum_recursion(n-1))
s = sum_recursion(int(input("input =>  ")))
print(s)

#fpojsdfhu
n = int(input("enter any number to print star in desending order = "))
for i in range(n):
    print("&" * (i+1))
