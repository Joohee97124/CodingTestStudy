# 1037
'''
약수 N = (입력받은 약수 중에 가장 작은 수) * (입력받은 약수중에 가장 큰 수)
1. 어떻게 여러 값을 한줄로 입력받는가 → 배열로 받기
2. 입력받은 애들중에 가장 큰 수를 어떻게 받아내는가 → max() 함수 이용

--> list로 받을 때 
① input().split() #한번에 두개 이상의 값을 입력받기 (문자열을 띄어쓰기로 나누어서 list에 담아줌)
          ------- spilt의 괄호에 넣는 값으로 문자열을 나누어 저장 (빈칸=띄어쓰기 기준)
② map(적용할함수, 반복가능한 자료형) #문자열을 list형으로 변환하기
      ------ int ---------- input().split()
'''

count_a= int(input())
#measure_a = list(input())
measure_a = list(map(int,input().split()))

max_a = max(measure_a)
min_a = min(measure_a)

print(max_a * min_a)
