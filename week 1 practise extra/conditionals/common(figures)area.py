figure = input("what type of figure is this ?")
# the measurement of the figure must be in meters .
match figure:
    case "circle":
        #ask the user first what is thhe radius ?
       y = float(input("what is raius ? "))
       #multiply the square of radius with 22/7 to get out the area ao the figure
       z=(22/7)*y*y
       print(str(z) + " meter square ")


    case "square":
       # ask the user first what is the length of the figure
       l = float(input("what is side ? "))
       # do square of the side to get out area of the figure
       d = l*l
       print(str(d) + " meter square")
    case "rectangle":
       # ask the user what is the length of the rectangle ?
       l= float(input("what is the length of rectangle ? "))
       # ask the user what is the width of rectangle ?
       w=float(input("what is the width of rectangle ?"))
       a=l*w
       print(str(a) + " meter square ")
    case "triangle":
       # it is for right angle triangle
       # ask the user what is the height of the triangle
       h=float(input(" what is the height of the triangle ?"))
       # ask the user what is the base of the triangle
       b=float(input("what is the lenghth of base ? "))
       f=(1/2)*b*h
       print(str(f) + " meter square ")
    case "cylinder":
       # this will calculate total surface area of the cylinder
       #ask the user what is the radius of the base of the cyliner ?
       s=float(input("what is the radius of the base of cylinder ? "))
       #ask the user what is the height of the cylinder ?
       t=float(input("what is the height of the cylinder ? "))
       m=(44/7)*s*s*t
       print(str(m) + " meter square")
    case "cube":
       #this will calculate total surface area of the cube
       #ask the user what is the side of the cube ?
       k=float(input("what is the side of the cube ? "))
       l=6*k*k
       print(str(l) + " meter square ")
    case "cuboid":
       #this will calculate total surface area of the cuboid
       #ask the user what is the height of the cuboid ?
       x=float(input("what is the height of the cuboid ?"))
       #ask the user what is the width of the cuboid ?
       y=float(input("what is the width if the cuboid ? "))
       #ask the user what is length of the cuboid ?
       z=float(input("what is the length of the cuboid ?"))
       m=2*(x*y + y*z +z*x)
       print(str(m) + " meter square ")
    case "cone":
       #this will calculate total surface area of the cone
       #ask the user what is radius of the cone
       r= float(input("what is the radius of the cone ? "))
       #ask the user what is the slant height of the cone
       s=float(input("what is the slant height of the cone ? "))
       import math
       y=math.sqrt(r**2 +s**2)
       print(str(y) + " meter square ")
    case "sphere ":
       #ask the user what is the radius of the sphere
       r =float(input("what is the radius of the sphere ? "))
       a = 4*(22/7)*r*r
       print(str(a) + " meter square ")
    case "hemisphere":
       #this will calculate total surface area of the hemisphere
       #ask the user what is the radius if the hemisphere
       r=float(input("what is the radius of the hemisphere ? "))
       a=3*(22/7)*r*r
       print(str(a) + " meter square")
    case _:
       # in this program the most common figures used from grade 6 to 12 is present
       #if user's input figure is not in this program than print the response
       print("  Sorry !!,this figure is not  updated in my program .  " )
