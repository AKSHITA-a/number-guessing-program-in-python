'''
Generator functions  : the Generator functions is same as the normal function but the place of the return we use yield .
                      Unlike regular functions that return a value all at once, generator functions produce a sequence of values
                      on-the-fly as needed. This makes them more memory-efficient and faster for certain use cases.
Here’s how generator functions work:

Syntax:
A generator function is defined like a normal function, but instead of using return, it uses the yield keyword.
If the body of a function contains yield, it automatically becomes a Python generator function.
Creating a Generator Function:
You can create a generator function using the def keyword and the yield keyword.
Example:
def func():
    yield 1
    yield 2
    yield 3
#for i in func():
 #   print(i)
a = func()
print(next(a))

Generator Expressions:
Another way to create generators is through generator expressions.
These use a similar syntax to list comprehensions but create generator objects instead of lists.
Example:
Python

# Generate multiples of 5 between 0 and 5 (divisible by 2)
generator_exp = (i * 5 for i in range(5) if i % 2 == 0)
for i in generator_exp:
    print(i)
AI-generated code. Review and use carefully. More info on FAQ.
Output:
0
10
20
                       '''
