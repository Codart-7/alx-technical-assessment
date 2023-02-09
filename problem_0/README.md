# Problem 0

## Problem Statement
You are preparing a cake but you don’t know how many teaspoons of sugar you will need to make it “perfect” or “not too sweet”.
In this case, find the first number of teaspoons that will make the cake “too sweet”.
For the first check, you add `n` teaspoons of sugar but it’s too sweet to your taste.
Unfortunately, you can’t rollback to a previous version of your cake by taking out teaspoons of sugar to adjust the sweetness to your cake.
However, you do have a tool to indicate if the current number of teaspoons of sugar will make your cake too sweet.
You want to redo this cake but to do so, you need to know at which point the number of teaspoons of sugar will make your cake too sweet.

You are given `n`, the number of teaspoons of sugar that the recipe states is required to make your cake and a function `isTooSweet(i)`, which returns `true` if `i` teaspoons of sugar makes your cake too sweet.
With these two pieces of information, find `x`, the first number of teaspoons of sugar that will make your cake too sweet.

### Extra clarifications:
- After `x` the cake is too sweet
- `n` is superior or equal to 1
- For any value of `n`, your cake will be always too sweet (`x` always exists)

## Solution Explanation
What I was given:
1) `n`: the number of teaspoons of sugar that the recipe states is required to make your cake
2) `isTooSweet`: returns true if i teaspoons of sugar makes your cake too sweet

### Base assumptions
- Since `n` can be equal to 1 and `n` is always "too sweet", then `x` can be less than 1.
- Since the caliberation of the teaspoon was not given, I assumed a value of 0.2.
- `x` is rounded to one decimal place.
- Based on the "Extra Clarifications" section, any value after `x` is "too sweet". This means that `x` is "not too sweet"

### Method
Recursive algorithm.

NB: I implemented a test `isTooSweet()` function to test