x=1
y=10
while x<y:
    x+=1
    if x%2==0:
        continue
    print("Akirachix")
    print(x)

x=range(10) 
for y in x:
    if y%2==0:
        print(f"{y} is an even number")
    else:
        print(f"{y} is an odd number")    


x=range(10) 
for y in x:
    if y%3==0:
        print(y)

x=range(20)
for y in x:
    if y%2==0:
        print(f"{y} is divisible by 2")
    elif y%3==0:
        print(f"{y} is divisible by 3") 
    else:
        print(f"{y} is not divisible by 2 or 3")
x=1
y=10
while x<y:
    print(x)
    print("Akirachix")
    x+=1

x=1
y=10
while x<y:
    print(x)
    print("Akirachix")
    if x==5:
        break
    x+=1   
       
    