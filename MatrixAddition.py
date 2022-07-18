
n=int (input("Enter the Number of Rows\n"))
m=int (input("Enter The Number of Column\n"))

arr1=[[0 for i in range(m)] for j in range (n)]
arr2=[[0 for i in range(m)] for j in range (n)]
arr3=[[0 for i in range(m)] for j in range (n)]


print('Enter',n*m,'elments of the first matrix\n')
for i in range(n):
    for j in range(m):
        arr1[i][j]=int(input())

print('Enter',n*m,'elments of the second matrix\n')
for i in range(n):
    for j in range(m):
        arr2[i][j]=int(input())

print('Enter',n*m,'elments of the second matrix\n')
for i in range(n):
    for j in range(m):
        arr3[i][j]=arr1[i][j]+arr2[i][j]
print ('The Final matrix after matrix addition is\n')
for k in arr3:
    print(k)



