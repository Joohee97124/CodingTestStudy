# 2576
'''
1. 7개 자연수 (int) 입력받기 : for문으로 7번 돌리기 
for문 내
 if 홀수면 그것들 합 (합을 받아내는 변수필요)  
   최소 찾기 (최소찾는 변수 필요)
--> 짝수가 7번 들어온 떄 (-1) 어케 print 해야할지 모르겠음,,
2. 
'''

list_s = []

for i in range (7):
  n = int(input())

  if (n%2==1):
    list_s.append(n)

if list_s:
  print(int(sum(list_s)))
  print(int(min(list_s)))
else:
  print(-1)
