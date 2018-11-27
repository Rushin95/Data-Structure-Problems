# return the lenght of longest common subsequence
def lcs(a,b):
    m = [[None]*(len(b)+1) for i in range(len(a)+1)]

    for i in range(len(a)+1):
    for j in range(len(b)+1):
      if i == 0 or j == 0:
        m[i][j] = 0
      elif a[i-1] == b[j-1]:
        m[i][j] = m[i-1][j-1] + 1
      else:
        m[i][j] = max(m[i][j-1], m[i-1][j])
    for x in m:
        print x
    print 'Length of LCS: ',m[len(a)][len(b)]

a = 'AGGTAB'
b = 'GXTXAYB'
lcs(a,b)
