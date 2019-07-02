p=input()
digit=0
alpha=0
for i in (p):
    if i.isalpha():
        alpha=1
    if i.isdigit():
        digit=1
if(alpha and digit==1):
    print("Yes")
else:
    print("No")

