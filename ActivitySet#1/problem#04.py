
def computepay(h,r):
  if h<40:
    pay= h*r
  elif h>40:
     pay = 40*r+(h-40)*1.5*r
        
     return pay
  
h = float(input("Enter hours? "))
r = float(input("Enter rate per hour? "))
    
pay = computepay(h, r)
print(pay)