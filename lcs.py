def inputfile():
     S1 = input("Enter String-1")
     S2 = input("Enter String-2")
     A = len(S1)
     B = len(S2)
     lcs(S1, S2, A, B)

def lcs(S1, S2, A, B):
    L = [[0 for x in range(B+1)] for x in range(A+1)]

    for i in range(A+1):
        for j in range(B+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i-1] == S2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    index = L[A][B]
     
    lcs = [""] * (index+1)
    lcs[index] = ""
    i = A
    j = B
    while i > 0 and j > 0:
         if S1[i-1] == S2[j-1]:
             lcs[index-1] = S1[i-1]
             i-=1
             j-=1
             index-=1
         elif L[i-1][j] > L[i][j-1]:
              i-=1
         else:
              j-=1
              
    print (" LCS of " + S1 + " and " + S2 + " is" + "".join(lcs), " Length of LCS", len( "".join(lcs)))  




print (inputfile())    

