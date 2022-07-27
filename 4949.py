'''
1. while true 로 "."이 들어오면 break
2. a 문자열 입력받고
3. 문자열a만큼 for문 돌리면서
4. "[" 또는 "(" 가 있으면
	→ stack에 append (insert)
5. "]"가 있으면
	→ stack 길이가 0이 아니고, [ 가 있으면 pop (remove)
	→ 아니면 ] 추가
6. ")"가 있으면
	→ stack 길이가 0이 아니고, (가 있으면 pop (remove)
	→ 아니면 ) 추가
'''

while True :
    a = input()
    stack = []

    if a == "." :
        break

    for i in a :
        if i == '[' or i == '(' :
            stack.append(i)
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop() 
            else : 
                stack.append(']')
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')