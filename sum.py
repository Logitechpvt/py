n=int (input("Enter any number\n"))
tot=0
while(n>0):
     d=n%10
     tot=tot+d
     n=n/10
print("Total Sum Of Digits Is:\n",tot)
