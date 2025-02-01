Q1 Accept a positive integer n as input and print a "number arrow" of
size n. For example, n = 5 should produce the following output:
1
1,2
1,2,3
1,2,3,4
1,2,3,4,5
1,2,3,4
1,2,3
1,2
1
You can assume that n is greater than or equal to 2 for all test
cases. Hint: range(5, 0, -1) is the sequence 5, 4, 3, 2, 1

n = int(input())
for i in range(1,n+2):
  for j in range(1,i):
    if j<i-1:
      print(j,end=',')
    else:
      print(j)
for i in  range(n,o,-1):
  for j in range(1,i):
    if j<i-1:
      print(j,end=',')
    else:
      print(j)
