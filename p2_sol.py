def is_magic(mat):
  # first get the dimension of the matrix
  m = len(mat)
  # the sum of the two diagonals
  d1sum, d2sum = 0, 0 
  for i in range (m):
    d1sum+= mat[i][i]
    d2sum+= mat[i][m - i - 1 ]

  if not(d1sum == d2sum):
    return 'NO'
  for  i in range(m):
    rsum ,csum = 0,0
    for j in range(m):
      rsum+= mat[i][i]
      csem+= mat[j][i]
  if not(rsum == csum == d1sum):
    return 'NO'
  return 'Yes'
