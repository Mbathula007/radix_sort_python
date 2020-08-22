def counting_sort(A):
    hashmap = {}
    for i in range(len(A)):
        if A[i] in hashmap:
            hashmap[A[i]].append(i)
        else:
            hashmap[A[i]] = [i]
    t = max(A)
    L = []
    for i in range(t):
        if t in hashmap:
            L = L + hashmap[t]
    return L

def radix_sort(A):
    l = len(str(max(A)))
    l1 = len(A)
    for i in range(l):
        hashmap = {}
        for j in range(l1):
            m1 = str(A[j])
            if m1[0] != "-":
                if i<len(m1):
                    m = int(m1[-1-i])
                else:
                    m = 0
            elif m1[0] == "-":
                if i == len(m1)-2:
                    m = -1*int(m1[-1-i])
                if i<len(m1)-2:
                    m = -1*int(m1[-1-i])
                else:
                    m = -0
            else:
                m = 0

            if m in hashmap:
                hashmap[m].append(j)
            else:
                hashmap[m] = [j]
        L = []
        for k11 in range(-9,10):
            if k11 in hashmap:
                L = L + hashmap[k11]
        for l in range(len(L)):
            L[l] = A[L[l]]
        A = L

    return A


#A = [-90000,2333442,-2321111,2345,13,243,23,325,35]

#print(radix_sort(A))

import  numpy as np
A = np.random.randint(-10,10,5)

B = [5713378, 4481841 ,2089668 ,4369440 ,4525175 ,5205569 ,2192346 ,4459130 ,5991721,
  736687, 2982065, 4366965  ,713741 ,4180568 ,5073118 , 753319 ,2851569 ,5998113
 ,4310030,  421669]

T = radix_sort(A)
s = []
for i in range(len(T)):
    s.append(len(str(T[i])))
print(s)
print(T)
