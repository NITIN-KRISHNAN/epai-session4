# Session 4 - Numeric Types II

**Qualean** class that is inspired by Boolean+Quantum concepts. We can assign it only 3 possible **real** states. True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state. The moment you assign it a real number, it immediately finds an imaginary number **random.uniform**(-1, 1) and multiplies with it and stores that number internally after using Bankers rounding to 10th decimal place

Magic methods of class Qualean are implemented

## \__init__

The \__init__ method is similar to constructors in C++ and Java. Constructors are used to initialize the object.

**test_valid_input** test case is used to check if the Qualean object is initialized properly.

1, -1, 0, 0.0, 1.0, -1.0 are the valid input values for Qualean object initialization.

This test checks negative use case of string, complex number and a number that is not in the list of valid inputs.

## boolean operators

The boolean operators (\_\_and_\_, \_\_or__ ) cannot be directly overidden in python, but the use case is acheived by overriding \_\_bool__ magic function.

## \__bool__

This returns false if the value if imaginary state is equal to 0 else true.

This method is also used when doing boolean operations such as and, or, not.

**test_bool** test case verifies if bool(Qualean(0)) is False

## \__and__

**test_and** test case checks the and functionality of with the possible inputs of Qualean.

Another point to be noted for **and** operation in python is that when the short circuit happens the value of the variable whose bool is **False** is returned.

q1 = Qualean(0)

q2 = Qualean(1)

q1=0E-10

q2=0.7186551638

q1 and q2 will return q1

q2 and q1 will return q1

as bool(q1) is False

##\__or__

**test_or** test case checks the and functionality of with the possible inputs of Qualean.

Another point to be noted for **or** operation in python is that when the short circuit happens the value of the variable whose bool is **True** is returned.

q1 = Qualean(0)

q2 = Qualean(1)

q1=0E-10

q2=0.7186551638

q1 or q2 will return q1

q2 or q1 will return q1

as bool(q1) is True

## \__repr__ and \_\_str__

both \_\_repr\__() and  \_\_str__() are string representations of the object

\_\_repr\__() is called when an object is printed in console and it is more useful for developers while \_\_str__() invoken when the object is printed and it is for end users.

## \__float__

float is an inbuilt numeric type, this function gets invoked when float(qua lean_object) is called.

## \__eq__

Checks if two qualean objects are equal

## \__ge__

greater than or equal to

## \__gt__

greater than

## \__invertsign__

inverts the sign of the imaginary state and returns the modified qualean object

## \__le__

less than or equal to

## \__lt__

less than

## \_\_add__

This function adds two Qualean objects, it can even add an integer to a Qualean object.

**test_add** test case checks if the sum of two Qualean objects is the sum of its respective imaginary states.

## \__mul__

multiplies the qualean object with another qualean object or any integer

test_sum_equals_product test case is added to validate this use case

## \__sqrt__

calculates the sqrt







