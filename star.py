#2438
n=int(input())
for i in range(1, n+1):  
    print('*' * i)


#2439
a=int(input())
for i in range(1,a+i):
    print(" "*(a-i) + "*"*i)


#2440
a=int(input())
for i in range(1,a+1):
    print("*"*(a-i+1))


#2441
a=int(input())
for i in range(1,a+1):
    print(" "*(i-1) + "*"*(a-i+1))


#2442
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*((2*i)-1))


#2443
n = int(input())
for i in range(n, 0, -1):
    print(' '*(n-i) + '*'*(2*i-1))


#2444
n=int(input())
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1))
for i in range(1,n):
    print(" "*i+"*"*(2*(n-i-1)+1))
