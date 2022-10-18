#Find the number of unique possible paths for the robot to reach at the bottom-right corner of the matrix if he starts from [0,0] position
#ex INPUT--row=3 colum=2 OUTPUT--POssible paths 3

def unique_paths(matrix,row,column):

    for i in range(row):#initializing the first row to 1
        matrix[i][0]=1
    for i in range(column):#initializing the first column to 1
        matrix[0][i]=1

    for i in range(1,row):#calculating the sum of the top and left block
        for j in range(1,column):
            matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]


    return(matrix[row-1][column-1])#the no. of paths is the present element of the [0,0] position

row,column=map(int,input().split(' '))
matrix=[[0]*column for i in range(row)]#way to change every element of matrix to 0

print(unique_paths(matrix,row,column))