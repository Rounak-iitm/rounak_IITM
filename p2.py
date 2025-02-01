A n×n square matrix of positive integers is called a magic square if the following sums are equal:
 row-sum: sum of numbers in every row; there are n such values, one for each row
 column-sum: sum of numbers in every column; there are n such values, one for each column
 diagonal-sum: sum of numbers in both the main diagonals; there are two values
There are n + n + 2 = 2n + 2 values involved. All these values must be the same for the matrix to be a
magic-square.
Write a function named is_magic that accepts a square matrix as argument and returns YES if it is
a magic-square and NO if it isn't one.
