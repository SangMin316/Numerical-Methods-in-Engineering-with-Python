import numpy as np
from numpy import random

A = np.random.rand(3,4) #3행 4열 행렬 random(0~1값)하게 생성
print(A)
a = A[0:3,0:3] # 0~3행 0~3열 요소를 받겠다 끝점 미포함
print(a)
b = A[:,3] #4열의 전체 요소를 받겠다.
print(b)

print(A.shape) # A의 모양 몇행 몇열인지 출력값: (3,4)
len(a) #첫번째 요소의 길이

aa = a.copy()   

a1 = [1,2,3]
b1 = a1 
a1.append(20) # 이렇게 해버리면 b1도 바뀜, 그래서 copy를 씀

a= np.array([[1.0, 1.0, 1.0],
             [2.0, 1.0, 2.0],
             [3.0, 1.0, 4.0]])
n = 3
for k in range(0,n-1):  #pivot rows, in range 마지막 은 포함 x, computer는 0부터 카운터
    for i in range(k+1,n):
        if a[i,k] != 0.0:
            #print('we are in loop',i,k)
            lam = a[i,k]/a[k,k] # Definition of lambda
            a[i,k:n] = a[i,k:n] - lam*a[k,k:n]    # a[i,k+1:n]까지 변경 for을 써도 되는되 numpy(a[i,k+1:n] 이런 형태)를 쓰면 훨씬 빠름

print(a)


A = np.random.rand(3,4) # 마지막 열을 b(미지수 x)로 두겠다
a = A[0:3,0:3] # 마지막 열을 뺀 요소를 계수로 보고, 그것을 a로 받겠다
aa = a.copy()

b = A[:,3] #4열의 모든 성분
bb = b.copy()
xx = b.copy()
x = np.zeros(len(b)) # x.shape(1,3)
n = len(a)
#Elimination phase
for k in range(0,n-1):  #pivot rows, in range 마지막 은 포함 x, computer는 0부터 카운터
    for i in range(k+1,n):
        if a[i,k] != 0.0:
            print('we are in loop',i,k)
            lam = a[i,k]/a[k,k] # Definition of lambda
            #a[i,k] = 0.0 # 소거
            a[i,k:n] = a[i,k:n] - lam*a[k,k:n]    # a[i,k+1:n]까지 변경 for을 써도 되는되 numpy(a[i,k+1:n] 이런 형태)를 쓰면 훨씬 빠름
            b[i] = b[i] - lam*b[k] # b[i]가 xi 임 연산할때 x도 같은 방법으로 바뀜

print('before\n',aa,'\n\n','after',a)
print('before\n',bb,'\n\n','after',b)

# Back substitution
for k in range(n-1,-1,-1): # form end to beginning , 0포함시키려고 
    x[k] = (b[k] - np.dot(a[k,k+1:n],x[k+1:n]))/a[k,k]  # j = k+1 ...., n 이게 솔루션임
    # 식을 전개 하면 a00*x0 +a01*x1 +...a0n*xn = b0 
    # x0 = (b0 - a01*x1 + ..+a0n*xn)/a00 이것을 array로 표현한게 위식이야 

print('x',x)


#함수로 만드는 것 

def gauss(a,b):
    for k in range(0,n-1):  #pivot rows, in range 마지막 은 포함 x, computer는 0부터 카운터
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                print('we are in loop',i,k)
                lam = a[i,k]/a[k,k] # Definition of lambda
                #a[i,k] = 0.0 # 소거
                a[i,k:n] = a[i,k:n] - lam*a[k,k:n]    # a[i,k+1:n]까지 변경 for을 써도 되는되 numpy(a[i,k+1:n] 이런 형태)를 쓰면 훨씬 빠름
                b[i] = b[i] - lam*b[k] # 
# Back substitution
    for k in range(n-1,-1,-1): # form end to beginning , 0포함시키려고 
        x[k] = (b[k] - np.dot(a[k,k+1:n],x[k+1:n]))/a[k,k]  # j = k+1 ...., n

    return x

print(gauss(aa,bb))


for k in range(0,n-1):  #pivot rows, in range 마지막 은 포함 x, computer는 0부터 카운터
    for i in range(k+1,n):
        if a[i,k] != 0.0:
            print('we are in loop',i,k)
            lam = a[i,k]/a[k,k] # Definition of lambda
            #a[i,k] = 0.0 # 소거
            a[i,k:n] = a[i,k:n] - lam*a[k,k:n]    # a[i,k+1:n]까지 변경 for을 써도 되는되 numpy(a[i,k+1:n] 이런 형태)를 쓰면 훨씬 빠름
            b[i] = b[i] - lam*b[k]

# upper traiangle gaussian elimination소거법

for k in range(n-1,0,-1): # 전체 열이고, n-1(맨끝)부터 0(처음)은 미포함
    for i in range(k-1,-1,-1): # k위부터 처음(0인데, 끝점 미포함으로 -1)까지 -1씩
        if a[i,k] != 0:
            lam = a[i,k]/a[k,k]
            a[i,k:n] = a[i,k:n] - lam*a[k,k:n] # i행의 맨끝부터 대각선까지의 열까지의 연산
            b[i] = b[i] -lam*b[k]

# 위 방법은 k 와 i를 바꿨으므로 Back substitution과 if문 안에 있는 식은 기존에 있던 식과 같다.

