num=int(input("enter the number"))
summ=0
while num!=0:
    temp=num%10
    summ=summ+temp
    num=num//10
print(summ)
            