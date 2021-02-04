# GildedRose Refactoring Kata


# Constraints
- It is not allowed to alter the Item class or Item Property

## General item constraints
- If the sell date is passed, quality of items decrease 2x faster
- The quality of an item can never be negative
- The quality of an item can never be more then 50

## Specific item constraints
- "Aged Brie" increases in quality by +1 the older it gets
    - When sell date is 0, the quality increases with +2 
- "Sulfuras" never decreases in quality nor needs to be selled
    - The quality is always 80
- "Conjured" decreases in quality by -2
    - When sell date is 0, the quality decreases with -4
- "Backstage passes" also increase in quality as they get older as followed:
    - When sell date is more then 10, the quality increases with +1
    - When sell date is 10 or less, the quality increases with +2
    - When sell date is 5 or less, the quality increase with +3

# Why refactor
- The code is messy and hard to read.
- It gives negative values

# Notes regarding my code
- the function should use return to output the results
- each item should have its own function
- contraints should not be hard coded in every item
- functions have type hints to provide the right data type

# Requirements
- Python 3.7.6


