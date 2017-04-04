
class matrix:
    def __init__(self, mat):
        self.mat = mat
        self.current=0
        
    def __str__(self):
        s = ''
        for x in range(len(self.mat)):
            for y in range(len(self.mat[0])):
                s += str(self.mat[x][y]) + ' '
            s += '\n'
        return s
    
    def __iter__(self):
        return self

    def next(self):
        if self.current >= len(self.mat):
            raise StopIteration
        else:
            self.current += 1
            return self.mat[self.current-1]

    
    def __add__(self, other):
        result = matrix([[0 for i in range(len(self.mat[0]))]for j in range(len(self.mat))])
        if(type(other) == type(self)):
            if((len(self.mat) == len(other.mat)) and (len(self.mat[0]) == len(other.mat[0]))):
                for i in range(len(self.mat)):
                    for j in range(len(self.mat[i])):
                        result.mat[i][j] = self.mat[i][j] + other.mat[i][j]
            else:
                print 'Error: the matrix must have the same size'
                result = None
        elif (type(other) ==int or type(other) ==float):
            for i in range(len(self.mat)):
                for j in range(len(self.mat[i])):
                    result.mat[i][j] = self.mat[i][j] + other
        else:
            print 'Error: the argument must be class matrix or int or float'
            print type(other)
            result = None
        return result
    
    def __sub__(self, other):
        result = matrix([[0 for i in range(len(self.mat[0]))]for j in range(len(self.mat))])
        if(type(other) == type(self)):
            if((len(self.mat) == len(other.mat)) and (len(self.mat[0]) == len(other.mat[0]))):
                for i in range(len(self.mat)):
                    for j in range(len(self.mat[i])):
                        result.mat[i][j] = self.mat[i][j] - other.mat[i][j]
            else:
                print 'Error: the matrix must have the same size'
                result = None
        elif (type(other) == int or type(other) == float):
            for i in range(len(self.mat)):
                for j in range(len(self.mat[i])):
                    result.mat[i][j] = self.mat[i][j] - other
        else:
            print 'Error: the argument must be class matrix or int or float'
            result = None
        return result
    
    def __radd__(self,other):
        if (type(other) == int or type(other) == float):
            result = matrix([[0 for i in range(len(self.mat[0]))]for j in range(len(self.mat))])
            for i in range(len(self.mat)):
                for j in range(len(self.mat[i])):
                    result.mat[i][j] = self.mat[i][j] + other
        else:
            print 'Error: the argument must be class int or float'
            result = None
        return result
    
    def __rsub__(self,other):
        if (type(other) == int or type(other) == float):
            result = matrix([[0 for i in range(len(self.mat[0]))]for j in range(len(self.mat))])
            for i in range(len(self.mat)):
                for j in range(len(self.mat[i])):
                    result.mat[i][j] = other - self.mat[i][j]
        else:
            print 'Error: the argument must be int or float'
            result = None
        return result
        
    def prod(self,mat_prod):
        if(type(mat_prod) == type(self)):
            row_per_column = 0
            if(len(self.mat[0]) == len(mat_prod.mat)):
                result = matrix([[0 for i in range(len(mat_prod.mat[0]))]for j in range(len(self.mat))])
                for i in range(len(self.mat)):
                    for j in range(len(mat_prod.mat[i])):
                        for h in range(len(self.mat[i])):
                            row_per_column += self.mat[i][h] * mat_prod.mat[h][j]
                        result.mat[i][j] = row_per_column
                        row_per_column = 0
            else:
                print 'error: the matrix must have the same size of the dimension n: m x n * n x p'
                result = None
        else:
            print 'Error: the argument must be class matrix'
            result = None
        return result

#1. pep8, https://www.python.org/dev/peps/pep-0008/ – your improved task must comply with pep8

#2. constructor
m1 = matrix([[1,1,1],[1,1,1],[1,1,1]])
m2 = matrix([[1,2,3],[1,2,3],[1,2,3]])
print '2. constructor:'
print 'matrix1'
print m1
print 'matrix2'
print m2

#2. constructor:
# matrix1
# 1 1 1 
# 1 1 1 
# 1 1 1 
#
# matrix2
# 1 2 3 
# 1 2 3 
# 1 2 3 

#3. add two matrices
print '3. add two matrices:'
m3 = m1 + m2
print m3

#3. add two matrices:
# 2 3 4 
# 2 3 4 
# 2 3 4 

#4. add scalar to matrix
print '4. add scalar to matrix:'
m3 = m1 + 5 
print m3

#4. add scalar to matrix:
# 6 6 6 
# 6 6 6 
# 6 6 6 

#5. add matrix to scalar
print '5. add matrix to scalar:'
m3 = 5 + m1
print m3

#5. add matrix to scalar:
# 6 6 6 
# 6 6 6 
# 6 6 6 

#6. subtraction
print '6. subtraction:'
m3 = m1 - m2
print 'sub two matrices:'
print m3
print 'sub scalar to matrix:'
m3 = m1 - 5
print m3
print 'sub matrix to scalar:'
m3 = 5 - m1
print m3

#6. subtraction:
# sub two matrices:
# 0 -1 -2 
# 0 -1 -2 
# 0 -1 -2 
#
# sub scalar to matrix:
# -4 -4 -4 
# -4 -4 -4 
# -4 -4 -4 
#
# sub matrix to scalar:
# 4 4 4 
# 4 4 4 
# 4 4 4 

#7. product of two matrices 
print '7. product of two matrices:'
m3=m1.prod(m2)
print m3

#7. product of two matrices:
# 3 6 9 
# 3 6 9 
# 3 6 9 

#8. Matrix iterable
print '8. matrix iterable'
for v in m1:
    print v

#8. matrix iterable
# [1, 1, 1]
# [1, 1, 1]
# [1, 1, 1]

#9. Make some lines that will show me that the changes above have been applied
