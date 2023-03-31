number=int(input("Enter a number:"))
string=str(number)
length=len(string)
values=[]
for i in string:
    intt=int(i)**length
    values.append(intt)
print(sum(values))
sum1=sum(values)
if number==sum1:
    print(f"{number} is armstrong number")
else:
    print(f"{number} is not a armstrong number")
