class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            return False

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0


def prior(n):
    if n == '**':
        return 4
    elif n == '*' or n == '/':
        return 3
    elif n == '+' or n == '-':
        return 2
    elif n == '(':
        return 1


def recognize(input):
    recognized = []
    numbers = '1234567890.'

    i = 0
    while i < len(input):
        j = 1
        if input[i] in numbers:
            while i+j < len(input):
                if input[i+j] in numbers:
                    j += 1
                else:
                    break
            recognized.append(''.join(input[i:i+j]))
            i += j
        elif input[i] == '*' and input[i+1] == '*':
            recognized.append(''.join(input[i:i+2]))
            i += 2
        else:
            recognized.append(input[i])
            i += 1
    return recognized


num = Stack()
post = []
input = input()
token = 0
recognized = recognize(input)
# 후위식으로 변환
# 숫자는 그냥 저장
# 문자가 나오면 스택에 쌓고, 그다음 문자가 나오면 그 전 문자와의 우선 순위를 비교후 낮다면
for i in recognized:
    # 여는괄호는 바로 넣음
    if i == '(':
        num.push(i)
    elif i == ')':
        # (가 나올때까지 연산자 추출
        while num.top() != '(':
            post.append(num.pop())
        # 여는 괄호는 그냥 뺌
        num.pop()
    elif i == '+' or i == '-' or i == '/' or i == '*' or i == '**':
        # top에 있는 연산자가 현재연산자의 우선순위보다 큰경우
        while (not num.isEmpty() and prior(num.top()) >= prior(i)):
            e = num.pop()
            post.append(e)
        num.push(i)
    else:

        post.append(i)
while not num.isEmpty():
    post.append(num.pop())

answer = Stack()
oper = ['+', '-', '*', '/', '**']
for i in post:
    if i in oper:
        if i == '**':
            # 다음 제곱이 끝나기까지 대기.
            answer.push(i)
        else:
            n1 = answer.pop()
            n2 = answer.pop()
            if i == '+':
                answer.push(n2+n1)
            elif i == '-':
                answer.push(n2-n1)
            elif i == '*':
                answer.push(n2*n1)
            elif i == '/':
                answer.push(n2/n1)
    else:
        answer.push(float(i))
print(answer.pop())
