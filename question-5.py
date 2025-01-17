'''5)Write a program which contains one class named as Numbers.
 Arithmetic class contains one instance variables as Value.
 Inside init method initialize that instance variables to the value which is accepted from user.
There are four instance methods inside class as ChkPrime(), ChkPerfect() , SumFactors(), Factors().
ChkPrime() method will returns true if number is prime otherwise return false
ChkPerfect () method will returns true if number is perfect otherwise return false.
Factors () method will display all factors of instance variable.
SumFactors() method will return addition of all factors. Use this method in any another method
As a helper method if required.
After Designing the above class call all instance methods by creating multiple objects.'''

class Numbers:
    def __init__(self, value):
        self.value = value

    def chk_prime(self):
        if self.value > 1:
            for i in range(2, int(self.value ** 0.5) + 1):
                if self.value % i == 0:
                    return False
            return True
        else:
            return False

    def chk_perfect(self):
        factors = self.factors()
        if sum(factors) == 2 * self.value:
            return True
        return False

    def factors(self):
        factors = []
        for i in range(1, int(self.value ** 0.5) + 1):
            if self.value % i == 0:
                factors.append(i)
                if i != self.value // i:
                    factors.append(self.value // i)
        return sorted(factors)

    def sum_factors(self):
        return sum(self.factors())


number1 = Numbers(28)
number2 = Numbers(7)


print(f"{number1.value} is prime: {number1.chk_prime()}")
print(f"{number1.value} is perfect: {number1.chk_perfect()}")
print(f"Factors of {number1.value}: {number1.factors()}")
print(f"Sum of factors of {number1.value}: {number1.sum_factors()}")

print(f"{number2.value} is prime: {number2.chk_prime()}")
print(f"{number2.value} is perfect: {number2.chk_perfect()}")
print(f"Factors of {number2.value}: {number2.factors()}")
print(f"Sum of factors of {number2.value}: {number2.sum_factors()}")
