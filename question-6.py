'''6)Write a program which contains one class named as Numbers.
 Arithmetic class contains one instance variables as Value1,Value2.
 Inside init method initialize all instance variables to 0.
There are three instance methods inside class as Accept(),Addition(),Subtraction(),Multiplication(),Division().
Accept method will accept value of value1 and value2 from user.
Addition() method will perform addition of Value1 and Value2 and return result.
Subtraction() method will perform subtraction of Value1 and Value2 and return result.
Multiplication() method will perform multiplication of Value1 and Value2 and return result.
Division() method will perform division of Value1 and Value2 and return result.
After Designing the above class call all instance methods by creating multiple objects.'''

class Numbers:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def accept(self):
        self.value1 = int(input("Enter value1: "))
        self.value2 = int(input("Enter value2: "))

    def addition(self):
        return self.value1 + self.value2

    def subtraction(self):
        return self.value1 - self.value2

    def multiplication(self):
        return self.value1 * self.value2

    def division(self):
        if self.value2 != 0:
            return self.value1 / self.value2
        else:
            return "Error: Division by zero"


numbers1 = Numbers()
numbers2 = Numbers()


numbers1.accept()
print(f"Addition: {numbers1.addition()}")
print(f"Subtraction: {numbers1.subtraction()}")
print(f"Multiplication: {numbers1.multiplication()}")
print(f"Division: {numbers1.division()}")

numbers2.accept()
print(f"Addition: {numbers2.addition()}")
print(f"Subtraction: {numbers2.subtraction()}")
print(f"Multiplication: {numbers2.multiplication()}")
print(f"Division: {numbers2.division()}")
