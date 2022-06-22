# 10818 
'''
1. 정수 개수 입력받기
2. 정수 입력받기 (1번의 개수만큼)
3. 최소값/최대값 찾기 -> 출력
'''

N = int(input())
N_input = list(map(int, input().split()))

min_N = min(N_input)
max_N = max(N_input)

print(min_N, max_N)
