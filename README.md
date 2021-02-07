# Gilded Rose Refactoring Kata
The Gilded Rose Kata is to improve your refactoring skills. The original kata can be found [here](https://github.com/emilybache/GildedRose-Refactoring-Kata).

The purpose of this exercise is to improve the current code by refactoring it, while keeping the constraints in mind.

# Why refactor the code?
- The code is messy and hard to read.
- Items are hard to distinguish in the code.
- Lots of nested if statements.
- Everything under 1 function.
- Code makes it hard to add new items.

# Constraints
This kata has some contraints that is involved in solving the exercise. The constraints are specified below. 

## Constraints original code
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

# My approach
 The first step was understanding what the original code did, and once this was clear I started writing unit tests. This is done to see if the original code behaves in the expected way. 

After the unit tests, the code can be refactored. I split the items in separate functions to define each item's logic and to make it more readable. By creating separated functions for each item it is easier to add new items with their own logic. 

The refactored code can be found in the `gilded_rose.py` and the unit tests in the `test_gilded_rose.py`.



# Requirements
- Python 3.7.6

# Setup and run tests
Setup virtual environment:

- **Create environment**
> python -m venv my_env

- **Activate environment**
> my_env\Scripts\activate

Run the unit tests:
> python -m unittest -v test_gilded_rose.py