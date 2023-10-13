class Gaus_Jordan():
    def __init__(self, matrix):
        self.matrix = matrix
    
    def printMatrix(self):
        print("\n")
        for i in self.matrix:
            for j in i:
                print(j, end="\t")
            print("\n")
    
    def getOne(self,p):
        for i in range(len(self.matrix[0])):
            if self.matrix[p][p] != 1:
                q = self.matrix[p][p]
                for j in range(len(self.matrix[0])):
                    self.matrix[p][j] = self.matrix[p][j] / q
    
    def setZero(self,r, c,):
        for i in range(len(self.matrix[0])):
            if self.matrix[r][c] != 0:
                q = self.matrix[r][c]
                for j in range(len(self.matrix[0])):
                    self.matrix[r][j] = self.matrix[r][j] - (q * self.matrix[c][j])
    

def check_solution(A, x):

  n = len(A)

  # Перевіряємо, чи виконується система рівнянь.
  for i in range(n):
    sum = 0
    for j in range(n):
      sum += A[i][j] * x[j]
    if sum != A[i][-1]:
      return False

  return True

def main():
  A = [[15.7, 6.6, -5.7, 11.5, -2.4],
       [8.8, -6.7, 5.5, -4.5, 5.6],
       [6.3, -5.7, -23.4, 6.6, 7.7],
       [14.3, 8.7, -15.7, -5.8, 23.4]]
  x = Gaus_Jordan(A)
  x.printMatrix()
  for i in range(len(A)):
    x.getOne(i)
    for j in range(len(A)):
        if i != j:
            x.setZero(j, i)
  x.printMatrix()
  A_M = [x.matrix[a][-1] for a in range(len(x.matrix))]

  print(check_solution(A,A_M))


    



if __name__ == "__main__":
  main()
