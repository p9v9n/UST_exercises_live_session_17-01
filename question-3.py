'''3)Write a program which contains one class named as Circle
Circle class contains three instance variables as Radius,Area ,Circumference.
That class contains one class variable as PI which is initialize to 3.14
Inside init method initialize all instance variables to 0.0
There are three instance methods inside class as Accept(), CalculateArea(), CalculateCircumference( ),
,Display( )
Accept method will accept value of Radius from user.
CalculateArea () method will calculate area of circle and store it into instance variable Area.
CalculateCircumference () method will calculate circumference of circle and store it into instance variable 
Circumference.
And Display( ) method will display value of all the instance variables as radius , Area , Circumference.
After designing the above class call all instance methods by creating multiple objects'''

class Circle:
    PI = 3.14  

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter the radius of the circle: "))

    def CalculateArea(self):
        self.Area = Circle.PI * (self.Radius ** 2)

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print(f"Radius: {self.Radius}, Area: {self.Area}, Circumference: {self.Circumference}")


circle1 = Circle()
circle1.Accept()
circle1.CalculateArea()
circle1.CalculateCircumference()
circle1.Display()

circle2 = Circle()
circle2.Accept()
circle2.CalculateArea()
circle2.CalculateCircumference()
circle2.Display()
