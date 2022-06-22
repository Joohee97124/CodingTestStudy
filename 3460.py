# 3460
'''
1. 양의정수 n 입력받기
2. n 을 2진수로 변환
3. 1의 인덱스 반환
'''

n = int(input())
n2=[]

# 2진수 만드는 함수 (예. 0b1101)
#n_bin = bin(n)
#print(n_bin)

# ob 없앤 이진수 만들기
n_bin=[]
n_bin = list(map(int,format(n,'b')))
print(n_bin)

# enumerate()함수 = 인덱스,값을 한꺼번에 얻을 수 있는 함수
for index, value in enumerate(n_bin):

  if value == 1 :
    ni = index

    # 1이 있는 인덱스를 n2 list에 넣기
    n2.append(ni)

# n2 list를 내림차순으로 정렬
n2.sort()

# n2 list를 출력하기 
for i2 in n2:
  print(i2, end=" ")