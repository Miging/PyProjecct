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
    if n=='*' or n=='/':
        return 3
    elif n=='+' or n=='-':
        return 2
    elif n=='(':
        return 1
def recognize(input):
    recognized=['']
    numbers=list('1234567890.')
    i=0
    while i<len(input):
       j=1
       if input[i] in numbers:
           while i+j<len(input):
               if input[i+j] in numbers:
                    j+=1
               else:
                   break
       else:
            recognized.append(''.join(input[i:i+j]))
            i+=j
    return recognized

    
num=Stack()
post=[]
input=input()
token=0
recognized=recognize(input)
#후위식으로 변환
#숫자는 그냥 저장
#문자가 나오면 스택에 쌓고, 그다음 문자가 나오면 그 전 문자와의 우선 순위를 비교후 낮다면  
for i in input:
    #여는괄호는 바로 넣음
    if i=='(':
        num.push(i)
    elif i==')':
        #(가 나올때까지 연산자 추출
        while num.top()!='(':
            post.append(num.pop())
        #여는 괄호는 그냥 뺌
        num.pop()
    elif i=='+' or i=='-' or i=='/' or i=='*':
        #top에 있는 연산자가 현재
        while(not num.isEmpty() and prior(num.top())>=prior(i)):
            e=num.pop()
            post.append(e)
        num.push(i)
    else:

        post.append(i)
while not num.isEmpty():
    post.append(num.pop())