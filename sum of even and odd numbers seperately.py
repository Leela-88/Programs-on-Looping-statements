num=int(input("enter the number "))
i=1
summ1=0
summ2=0
while i<=num:
    if i%2==0:
        summ1=summ1+i
    else:
        summ2=summ2+i
        
    i=i+1
print(summ1)
print(summ2)
   