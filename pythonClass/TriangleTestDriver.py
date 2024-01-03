# @Gabriel Haro-Villa
# This program tests the Triangle class
from Triangle import Triangle

def main():
    print("Test default constructor parameters, __str__, and getArea")
    triangle1 = Triangle()
    print(triangle1)
    print(f"Triangle Area: {triangle1.getArea():,.2f} square units")
    
    print("\nTest invalid arguments to setters")
    try:
        triangle1.setBase(-1)
        print(triangle1)
    except Exception as exc:
        print(exc)
    try:
        triangle1.setHeight(0)
        print(triangle1)
    except Exception as exc:
        print(exc)


    print("\nTest invalid arguments to constructor")
    try:
        triangle2 = Triangle(-3,4)
        print(triangle2)
    except Exception as exc:
        print(exc)
    try:
        triangle2 = Triangle(3,0)
        print(triangle2)
    except Exception as exc:
        print(exc)        

    print("\nTest valid float constructor parameters, __str__, and getArea")
    triangle3= Triangle(3.3,5.2)
    print(triangle3)
    print(f"Triangle Area: {triangle3.getArea():,.2f} square units")
main()