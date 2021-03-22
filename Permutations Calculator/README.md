The permutation calculator takes in an array of objects and the number of items to pick from that array. For example: `{a, b, c}` pick `2`.  You can use the permutation calculator in different ways to retrieve permutations. You can interate over the calculator to retrieve all the permutations one at a time. You an also retrieve the Nth permutation or a random permutation.  The permutation calculator imposes a certain order to the permutations.  For example a random permutation of `{a, b, c}` pick `2` is `{b, a}`.

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

Instructions `0 0 0` would produce `{A, B, C}`
Instructions `0 0 1` would produce `{A, B, D}`
Instructions `0 1 0` would produce `{A, C, B}`
Instructions `0 1 1` would produce `{A, C, D}`
Instructions `0 2 0` would produce `{A, D, B}`
Instructions `0 2 1` would produce `{A, D, C}`
And so on...

Lets look how the calculator processes the instructions `0 1 0` over the set `{A, B, C, D}`, as an example:
1. The first 0 in `0 1 0` tells the calculator to pop the 0th item from `{A, B, C, D}` and put it into the result set `{}`, so we end up with `{B, C, D}` and `{A}`
2. The second

There are two algorithms in use in the class. Both of which I entirely thought of and created myself, but only one works for all cases.

### The First Algorithm ###
(I thought of this one after 5 minutes of thinking about it in bed)

The ideas in this algorithm work for every case, and is used by these functions: `next()`, `reset()`, and `random()`.

Let there be a set of four items, `{a, b, c, d}`, with a pick of 4.
Let there be another set where we will build our permutations.
To construct the first permutation, we will start with the obvious first item, `a`, and pop it from the set.
The permutation so far is `{a}`, and the set is `{b, c, d}`.
Next, we are going to take the next obvious item, `b`, and again pop it from the set.
Permutation: `{a, b}`
Set: `{c, d}`
The process repeats for `c` and `d`, successfuly creating our first permutation of `{a, b, c, d}`.
Now we will reset the set to `{a, b, c, d}` and build our second permutation.

We will keep the steps from the first permutation and end up with these sets:
Permutation: `{a, b}`
Set: `{c, d}`
After this point, if we choose `c` as our next item, `d` will be the only one left and the permutation will be the same, so we know the `d` must be the same item, followed by `c`.
Permutation: `{a, b, d, c}`
Set: `{}`
And there's our second permutation!

To create our third permutation, we will repeat the starting steps, but only this far:
Permutation: `{a}`
Set: `{b, c, d}`
If we choose `b` as our next item, the only two items to choose from after that are `c` and `d`, which woule create the permutations `{a, b, c, d}` and `{a, b, d, c}`, which we already found.
We know that the next item cannot be `b`, so the next obvious choice is to choose `c`, and, as usual, pop it from the set.
Permutation: `{a, c}`
Set: `{b, d}`
The next obvious items are `b` and `c`.
Permutation: `{a, c, b, d}`
Set: `{}`
So `{a, c, b, d}` is our third permutation.

Following our logic from the second permutation, all we need to do to find the fourth permutation is copy the items from the previous permutation until there isn't room for change, and then choose the item after the item that doesn't allow for change, and follow our basic logic for the remaining items.
This means our fourth permutation will be the third permutation except with the last two values switched: `{a, c, d, b}`
And then for the fifth permutation, we can only use the first item, then need to jump to `d`.
Permutation: `{a, d}`
Set: `{b, c}`
The rest of the items are obvious, making the permutation `{a, d, b, c}`.
These patterns continue until the final permutation, (4! / (4 - 4)! = 24th permutation), `{d, c, b, a}`.

### The Second Algorithm ###
(This one took me a few days to come up with and refine)

This algorithm only works if the difference of the length of the set and the pick is 0, 1, or 2, or if the pick is 1 or 0.
This algorithm is used in the `permutation_at(int index)` and `set_next(int index)` functions.

Where `s` is the length of the set and `p` is the pick, the array of indexes is:
<img src="https://render.githubusercontent.com/render/math?math=f(x) = x%2B\sum_{i = 1}^{p - 1}{10^i - (i%2Bs - p)10^{i - 1} floor(x / (i%2Bs - p)! / round(s / p))}">

