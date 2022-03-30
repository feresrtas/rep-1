sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

if satır==0 or satır==3 or satır==6 or satır==9:
	      print('-  -  -  -  -  -  -  -  -  -  -  -  -')
satır=0
for t in range (0,9):
  j=0
  
  for i in sudoku[t]:   
    print (i,' ','',end='' )  
    j+=1
    if j==3 or j==6:
      print ('|','',end='' )
    elif j==9:
      print ('')  
      j+=1
      satır+=1
      if satır==0 or satır==3 or satır==6 or satır==9:
	      print('-  -  -  -  -  -  -  -  -  -  -  -  -')
        #dfgdfgdgdgdgdgdf
      
        
