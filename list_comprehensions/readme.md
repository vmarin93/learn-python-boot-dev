# List comprehensions

List comprehensions are a way of working with lists in Python. They help us write more succinct code in certain situations.

Say we need to write a program that given a list of numbers as input, returns a list of squares. We could write something like:

```
def get_squares(numbers: list) -> list:
	squares = []
	for num in numbers:
		squares.append(num ** 2)
	return squares
```

In this particular example, a list comprehension could help us reach the same result without having to write a for loop.

```
def get_squares(numbers: list) -> list:
	squares = [num ** 2 for num in numbers]
	return squares
```

## What is happening here?

First, we declare the transformation we want to happen `num ** 2` (we call this the "expression"), and after, we iterate over the elements that need to be transformed `for num in numbers` (we call this the "for clause").

And what about creating the squares list `squares = []` and then appending the transformed value to it `squares.append(num ** 2)`? Well, notice how in the list comprehension we wrapped the whole "inverted for loop" in brackets `[num ** 2 for num in numbers]`. This syntax is telling Python to create a list and append to it the values we are creating with the expression.

## Assignment

The party leader has activated a temporary buff that doubles the attack power of everyone in the party. Your task, should you choose to accept it, is to write a function that applies the buff to all the attacks using a list comprehension instead of a for loop.
