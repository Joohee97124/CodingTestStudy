#백준 18258 큐

import sys
from collections import deque

n = int(sys.stdin.readline())
qu=deque([])

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        qu.append(command[1])
    elif command[0] == 'pop':
        if len(qu)==0:
            print(-1)
        else:
            print(qu.popleft())
    elif command[0] == 'size':
        print(len(qu))
    elif command[0] == 'empty':
        if len(qu)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(qu) == 0: 
          print(-1)
        else: 
          print(qu[0])
    elif command[0] == 'back':
        if len(qu) == 0: 
          print(-1)
        else: 
          print(qu[-1]) 

