def max_operations(N, A):
    operations = 0
   
    while all(a % 2 == 0 for a in A):
        A = [a // 2 for a in A]
        operations += 1
   
    return operations




N = int(input())
A = list(map(int,input().split()))
print(max_operations(N,A))