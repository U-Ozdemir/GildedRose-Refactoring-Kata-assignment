# Gilded Rose Refactoring Kata
The Gilded Rose Kata is to improve your refactoring skills. The original kata can be found [here](https://github.com/emilybache/GildedRose-Refactoring-Kata).

The purpose of this exercise is to improve the current code by refactoring it, while keeping the constraints in mind.

# Constraints
This kata has some contraints that is involved in solving the exercise. The constraints are specified below. 

## Constraints existing code
- It is not allowed to alter the Item class or Item Property.

## General item constraints
- If the sell date is passed, the quality of items decrease 2 times faster.
- The quality of an item can never be negative.
- The quality of an item can never be more then 50.

## Specific item constraints
- "Aged Brie" increases in quality by +1 the older it gets.
    - When sell date decreases from 0, the quality increases with +2.
- "Sulfuras" never decreases in quality nor needs to be selled.
    - The quality is always 80.
- "Conjured" decreases in quality by -2.
    - When sell date decreases from 0, the quality decreases with -4.
- "Backstage passes" also increase in quality as they get older as followed:
    - When sell date is more then 10, the quality increases with +1.
    - When sell date is 10 or less, the quality increases with +2.
    - When sell date is 5 or less, the quality increase with +3.

# Why refactor the code?
- The code is messy and hard to read.
- Items are hard to distinguish in the code.
- Lots of nested if statements.
- Everything under 1 function.
- Code makes it hard to add new items.

# My approach
I started by setting up my environment in VSC first and created a virtualenv. 

**Activate venv**
> .\venv\Scripts\activate

After that I started to structured the code in a more readable way in the gilded_rose.py.

Next step will be writing functions for unittesting in test_gilded_rose.py.

# Notes regarding my code
- Needs separate functions for each item to make it more readable.
- Current solution does not use a return to output the results.
- Contraints should not be hard coded in every item.
- Functions should have type hints to provide the right data type.

# Requirements
- Python 3.7.6


