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
    
num=Stack()
post=Stack()
input=input()
token=0
#후위식으로 변환
#숫자는 그냥 저장
#문자가 나오면 스택에 쌓고, 그다음 문자가 나오면 그 전 문자와의 우선 순위를 비교후 낮다면  
for i in input:
    #연산자라면
    if i=='+' or i=='-' or i=='/' or i=='*':
        #전에 있던 연산자보다 우선순위가 낮다면 그 출력
        token=0
        while(post.top() and prior(post.top())>=prior(i)):
            e=post.pop()
            print(e,end='')
        post.push(i)
    else:
        print(i,end='')
while not post.isEmpty():
    print(post.pop(),end='')
