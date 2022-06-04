#1546
'''
M=최댓값 , 점수/M*100
0. 과목수 , 점수 입력받기 
1. 점수 수정하기 
2. 평균구하기 (수정된점수합/과목수)
'''

subject = int(input())
score = list(map(int,input().split()))

M=max(score)

score2=[]

for i in score :
  score2.append(i/M*100)

sum_new = int(sum(score2))
avg_new = sum_new / subject

print(avg_new)