QUESTION : Inverted Pyramid of Numbers Pattern
  
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5

CODE :
  
rows = 5

b = 0

for i in range(rows, 0, -1):

    b += 1

    for j in range(1, i + 1):

        print(b, end=' ')

    print('\r')
