The permutation calculator takes in an array of objects and the number of items to pick from that array. For example: `{A, B, C, D}` pick `3`.  You can use the permutation calculator in different ways to retrieve permutations. You can iterate over the calculator to retrieve all the permutations one at a time. You can also retrieve the Nth permutation or a random permutation.  The permutation calculator imposes a certain order to the permutations.  For example the 2nd permutation of `{A, B, C, D}` pick `3` is `{A, C, B}`.

The public functions are as follows:
 - The `next()` function returns the next permutation
 - The `reset()` function resets the calculator so that a subsequent call to `next()` returns the first permutation
 - The `permutation_at(int index)` function returns the permutation at the given index
 - The `set_next(int index)` function sets the index to use for the next call of `next()`
 - The `random()` function returns a random permutation
 - The `factorial(int n)` function returns the factorial of an integer (and returns 1 for netagive values)

### My Solution ###

My solution uses a set of instructions to the calculator to build a particular permutation. For example the instruction `0 1 0` to the set `{A, B, C, D}` produces the permutation `{A, C, B}`.

If the calculator was asked to pick `3` from the set `{A, B, C, D}` then it would use the following instructions to figure out the permutations:

- Instructions `0 0 0` would produce `{A, B, C}`
- Instructions `0 0 1` would produce `{A, B, D}`
- Instructions `0 1 0` would produce `{A, C, B}`
- Instructions `0 1 1` would produce `{A, C, D}`
- Instructions `0 2 0` would produce `{A, D, B}`
- Instructions `0 2 1` would produce `{A, D, C}`
- And so on...

Let's look at how the calculator processes the instructions `0 1 0` on the set `{A, B, C, D}` to produce the resulting permutation `{A, C, B}`. The numbers in the instructions tell the calculator which index to pop out of the set and add into the resulting permutation.  It processes the instructions left to right.
1. Start with the following - Instructions: `0 1 0` Set: `{A, B, C, D}` Permutation: `{}`
2. After processing the zero - Instructions: `1 0` Set: `{B, C, D}` Permutation: `{A}` (A at index 0 poped out of set and added to permutation)
3. After processing the one - Instructions: `0` Set: `{B, D}` Permutation: `{A, C}` (C at index 1 poped out of set and added to permutation)
4. After processing the zero - Instructions: ` ` Set: `{D}` Permutation: `{A, C, B}` (B at index 0 poped out of set and added to permutation)

Also note that the instructions are ordered as follows:
- 0th permutation is produced by instructions `0 0 0`
- 1st permutation is produced by instructions `0 0 1`
- 2nd permutation is produced by instructions `0 1 0`
- 3ed permutation is produced by instructions `0 1 1`
- 4th permutation is produced by instructions `0 2 0`
- 5th permutation is produced by instructions `0 2 1`
- And so on...

For each instructions pattern I figured out how to get the next instructions pattern. For example after pattern `0 2 0` comes pattern `0 2 1`.  I use this logic to implement the `next()` function.

I also figured out given an index how to get its corresponding instructions pattern.  For example how to get `0 2 1` for the 5th index.  I use this logic to implement the `permutation_at(int index)` and `set_next(int index)` functions.  This mathematical formula is quite complex and only works for picking 0, 1, N-2, N-1, or N items from a set with N items.

x = the index of the permutation (example: give me the 5th permutation)
s = the length of the set (example: 4 for set `{A, B, C, D}`)
p = the number of items to pick from the set (example: pick 3 items)
f(x) = the instructions pattern to apply on the set to get the xth permutation (example: 21, which left padded is `0 2 1`)

<img src="https://render.githubusercontent.com/render/math?math=f(x) = x%2B\sum_{i = 1}^{p - 1}{10^i - (i%2Bs - p)10^{i - 1} floor(x / (i%2Bs - p)! / round(s / p))}">

So for example:
- f(0) = 0 which translates to `0 0 0` after left-padding
- f(1) = 1 which translates to `0 0 1` after left-padding
- f(2) = 10 which translates to `0 1 0` after left-padding
- f(3) = 11 which tranlates to `0 1 1` after left-padding
- f(4) = 20 which translates to `0 2 0` after left-padding
- f(5) = 21 which translates to `0 2 1` after left-padding
