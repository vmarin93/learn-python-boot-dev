# Enumerate

Enumerate will keep a counter for us when looping through a list, returning both the state of the counter and the item in the list for each loop.

## Why?

Let's assume we are building a calendar app. We want to show the user the month's full name alongside its number. We could do something like this:

```
months = ["January", "February", "March"]
number = 1
for month in months:
	print(f"{number}: {month}")
	number += 1
```

Here, we have the list of full month names, and then we keep a counter that we increment for each month in the list.

## Better way?

```
months = ["January", "February", "March"]
for number, month in enumerate(months):
	print(f"{number}: {month}")
```

No more need to declare a variable that we have to increment. Enumerate is taking care of that for us. However, if you run the code above you will be disappointed with the results. Can you guess why?

```
0: January
1: February
2: March
```

Just like indexes in the list that start at 0, so does the counter that `enumerate` will keep for us. There is a fix though. `enumerate` takes in an optional argument called `start`:

```
months = ["January", "February", "March"]
for number, month in enumerate(months, start=1):
	print(f"{number}: {month}")
```

And the result we actually wanted:

```
1: January
2: February
3: March
```

## Assignment

We are working on a new feature that is going to show a live damage meter with rankings for the players in the party whilst fighting a boss. One of the other engineers wrote the code that gets the player's name and their dps (damage per second). Their function returns a list of dictionaries with each dictionary containing a player's name and its dps. The list is already sorted such that the player with the highest dps is first in the list.

```
players = [
    {"name": "Arannis", "dps": 4820},
    {"name": "Calyssa", "dps": 3190},
    {"name": "Borin", "dps": 2750},
]
```

We need to write the function that will display the damage meter on the screen with rankings.

```
1. Arannis - 4820 dps
2. Calyssa - 3190 dps
3. Borin - 2750 dps
```
