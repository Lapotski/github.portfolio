#initiate rectangle variables
recWicth=0
recHeight=0
recPerimeter=0
recArea=0
#initiate circle variables
PI=3.14159
cirRadius=0

print ("Enter the dimensions of the rectangle:")
recWidth=float(input("Rectangle Width: "))
recHeight=float(input("Rectangle Height: "))
recPerimeter=recWidth*recHeight
recArea=2*(recWidth+recHeight)

print("Enter the radius of the circle:")
cirRadius=float(input("Cicle Radius: "))
cirArea=PI*(cirRadius**2)
cirCircumference=2*PI*cirRadius

print("Rectangle:\nPerimeter:",recPerimeter,"\nArea:",recArea)
print("Circle:\nArea:",cirArea,"\nCircumference:",cirCircumference)