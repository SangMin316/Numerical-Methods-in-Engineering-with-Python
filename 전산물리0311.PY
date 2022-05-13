import numpy as np
# numpy array는 연산을 캐쉬 메모리안에서 해서 접근이 빠르다
# list 로 할떄도 행우선 연산인지, 열우선 연산인지에 따라 속도가 다름
# 이유는 블록단위로 캐쉬메모리에 정보를 올리기 때문에
A_np = np.ones((3000,3000)) 
import time

start_time =time.time

for i in range(3000):
    for j in range(3000):
        A_np[i,j] = A_np[i,j] + 1

end_time = time.time

print(end_time-start_time)



#LU decomposition

#A = [4,3]  L = [1,0]     U = [U11, U12]
#    [6,3]      [L21,1]       [0 ,U22]
# LU = [U11, U12]
#      [U11*L12, L12*U12 + U22]
# U11 = 4, U12 = 6, L21 = 6/4, U22 = -3/2 

L = np.array([[1,0],[6/4,1]])
U = np.array([[4,6],[0,-3/2]])

print(L*U) 

# A를 LU분해하시오
# A = [1,4,1]
#     [1,6,1]
#     [2,-1,2]

import scipy as sp
import scipy.linalg
sp.linalg.lu(A) # 출력은 permitation된 함수, L, u 
#permitation 해야하는데 
