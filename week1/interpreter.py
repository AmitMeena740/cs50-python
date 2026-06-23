Expression = (input("Expression : "))
#get the expression from the user which he/she want to solve

x, y, z = Expression.split(" ")
x = int(float(x))
#int for tell thhe computer first and second number is integer
z = int(float(z))
if y  == "+" :
  print(round(float(x + z) ,1))
  #for rounding off the answer to nearest decimal value
elif y == "-" :
    print(round(float(x - z) ,1))
elif y == "*" :
     print(round(float(x*z) ,1))
elif y == "/" :
   print(round(float(x/z) ,1))
else :
   print("Enter a valid operator ")
