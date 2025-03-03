#matrix 1
no_row1=int(input("No. of rows in 1st matrix: "))
no_column1=int(input("No. of columns in 1st matrix: "))
p=1
k=0
r1=no_row1
rownum = 1

print("row no. ", rownum, ":")
m1=[list(map(int, input(" ").split()))]
r1 -= 1
rownum +=1

while r1!=0:
    print("row no. ", rownum, ":")
    m1_1=list(map(int, input(" ").split()))
    
    r1 -= 1
    rownum +=1
    m1.append(m1_1)
    
    print(m1[p][k])
#--------------------------------------------------------------------
#matrix 2
no_row2=int(input("No. of rows in 2nd matrix: "))
no_column2=int(input("No. of columns in 2nd matrix: "))

r1=no_row2
rownum = 1

print("row no. ", rownum, ":")
m2=[list(map(int, input(" ").split()))]
r1 -= 1
rownum +=1

while r1!=0:
    print("row no. ", rownum, ":")
    m2_1=list(map(int, input(" ").split()))
    
    r1 -= 1
    rownum +=1
    m2.append(m2_1)
    print(m2[1][1])
#---------------------------------------------------------------------

answer=[]
temporary = [m1[0][0]*m2[0][0]]
temporary_2= [m1[0][1]*m2[1][0]]

temporary = list(map(str,temporary))
temporary_2 = list(map(str,temporary_2))

temporary = ''.join(temporary)
temporary_2 = ''.join(temporary_2)

temporary = int(temporary)
temporary_2 = int(temporary_2)


temporary=temporary+temporary_2
answer = answer + temporary

print(answer)
