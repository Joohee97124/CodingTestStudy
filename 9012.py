'''
1. 입력받을 수의 N(개) 받기
2. for N만큼 반복 //하면서	
	: 괄호 입력받기 (list)
3. list의 한 요소가 "(" 면 sum+1 ")" 면 sum-1
4. sum이 0 일때 YES / 0 아니면 NO
'''


import sys

N = int(sys.stdin.readline())
pr = []

for k in range (N)  :
  ps = list(sys.stdin.readline())
  sum=0
  
  for i in ps :
    if i==('(') :
      sum += 1
    elif i==(')'):
      sum -= 1
       
    if sum <0 :
        print("NO")
        break
    
  if sum==0 :
    print("YES")
  elif sum>0:
    print("NO")