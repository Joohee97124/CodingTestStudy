#10773 제로

'''
1. 입력 받을 숫자의 개수 입력받기 N
2. N만큼 for문 돌면서 
  - 숫자 입력받기 (list에 추가)
  - 이때 숫자가 0이면 이전 칸(스택)에 있던 애 삭제 
3. list에 남은애들로 합 계산 -> print
'''

N = int(input())
li=[]

for i in range (N):
  n=int(input())
  
  if n!= 0 :
    li.append(n)
  elif n==0 :
    li.pop()


print(sum(li))