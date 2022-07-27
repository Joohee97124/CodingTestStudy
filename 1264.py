'''
1. while true로 무한루프
	: # 입력받을 경우 break
2. 문자열 한 줄 받기
3. (2)의 문자열에서 모음 aeiou(대소문자) 의 개수 세기
4. print (3)의 개수
'''

while 1:
	cnt = 0
    s = input()
    
    if s == '#':
        break
    
    for c in s:
        if c in 'aeiouAEIOU':
            cnt += 1
            
    print(cnt)