#Sign your name: Danny H


# 1.) Write a program that asks someone for their name and then prints their name to the screen?
UserName=input("What is your name?")
print("Nice to meet you,", UserName)


# 2. Write a a program where a user enters a base and height and you print the area of a triangle.
TriangleBase=float(input("What is the base length of your Triangle?"))
TriangleHeight=float(input("What is the height of your Triangle?"))
Area=(TriangleBase*TriangleHeight)/2
print("The area of your Triangle is", Area)


# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
RadiusCircle=float(input("What is the radius of your circle?"))
DiameterCircle=RadiusCircle*2
CircumferenceCircle=DiameterCircle*3.14
print("The circumference of your circle is", CircumferenceCircle)


# 4. Ask a user for an integer and then print the square root.
FavoriteInteger=int(input("What is your favorite integer?"))
SRFI=FavoriteInteger**0.5
print("The square root of", FavoriteInteger, "is", SRFI)

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
print("May the mass times acceleration be with you!")
Mass=float(input("What is the mass?"))
Acceleration=float(input("What is the acceleration?"))
Force=Mass*Acceleration
print("Your force is", Force)
print("Get it?, that joke is okay but here is a better one.")
print("Where do you hide something from a Star Wars Fan?")
print("Inside The Phantom Menace dvd box")
