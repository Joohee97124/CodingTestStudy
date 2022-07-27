'''
1. n 숫자를 입력받고
2. for n번 돌리면서 deque 를 만든다
3. 길이가 1보다 크면
4. 맨위에 있는거 버리고 -> 그다음 애를 젤 아래로 보낸다
5. 버린 뒤 위에 있는 애를 num에 넣고 popleft → append
'''

from collections import deque
n = int(input())
que=deque()

for i in range(n):
  que.append(i+1)

while(len(que)>1):
  que.popleft()
  num=que[0]
  que.popleft()
  que.append(num)

print(que[0])