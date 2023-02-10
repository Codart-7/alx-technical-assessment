# Problem 1

## Problem Statement
Imagine you have a special keyboard with the following keys:
- Key 1: (`A`): Print one ‘A’ on screen
- Key 2: (`Ctrl-A`): Select everything printed in the whole screen
- Key 3: (`Ctrl-C`): Copy selection to buffer
- Key 4: (`Ctrl-V`): Print buffer on screen appending it after what has already been printed.
You can only press the keyboard for `N` times, find out the maximum numbers of ‘A’ you can print on screen.

**Example 1**:
```
Input: N = 2
Output: 2 -> for the sequence: A, A
```
**Example 2**:
```
Input: N = 7
Output: 9 -> for the sequence: A, A, A, Ctrl-A, Ctrl-C, Ctrl-V, Ctrl-V
```

### Extra clarifications:
- 1 <= N <= 50
- Answers will be in the range of 32-bit signed integer.

## Solution Explanation
`Ctrl-A`, `Ctrl-C` and `Ctrl-V` have to be consecutive for a meaninful result. That takes 3 key strokes.
For any `n` equal to or below 5, only `A`s make sense.
At `n` = 6, we observe a behaviour: 6 `A`s give the same result as 3 `A`s and `Ctrl-A`, `Ctrl-C` and `Ctrl-V`.
The pattern is repeatable and the goal is to use this to increase the buffer.

For example, after `n` = 6, it is safe to continue using `Ctrl-V`
But at `n` = 10, the result is 18, which is the same as replacing the last 3 elements of sequence with `Ctrl-A`, `Ctrl-C` and `Ctrl-V`. This is used to increase the buffer.