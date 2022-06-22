#10809
'''
1. S 문자 입력받기 -> 소문자 하나씩 list로
2. a~z 가있는 abc 문자열 만들기
3. for a~z와 (if) s를 비교하며  
   --> a~z와 s가 같으면 s의 index를 abc자리에 출력
   --> 없으면 -1 출력
'''

S = input()
print(S)
abc ='abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in S:
        print(S.index(i), end= ' ')
    else:
        print( -1, end =' ')
