p=10000
n=12
r=.08
t=int(input("Enter the number of years that you would like the money to be compounded for "))
a=p*(1+r/n)**(n*t)
print ("Your final value is: "+"$ "+str(a))