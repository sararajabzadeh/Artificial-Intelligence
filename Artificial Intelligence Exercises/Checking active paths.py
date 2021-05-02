def neighbor_checking(dic, node, seen):
    if node in seen:
        return False
    if node in dic:
        for neighbors in dic[node]:
            if not neighbor_checking(dic, neighbors, seen):
                return False
    return True

n , m = map(int,input().split())
# print(n,m)
dic ={}
for i in range(m):
    t1 , t2 = input().split()
    if t1 in dic:
        dic[t1] += [t2]
    else:
        dic[t1] =[t2]
# print(dic)

q = int(input())
# print(q)
masir=[]
seen=[]

for i in range(2*q):

    if i%2==0:
        masir = input().split()
    else:
        seen = input().split()
        array = [True]*(len(masir)-2)

        for j in range(len(masir)-2):

            temp = masir[j:j+3]

            if temp[0] in dic and temp[1] in dic and temp[1] in dic[temp[0]] and\
                    temp[2] in dic[temp[1]] and temp[1] in seen:
                array[j] =False


            elif temp[1] in dic and temp[2] in dic and temp[0] in dic[temp[1]] and\
                    temp[1] in dic[temp[2]] and temp[1] in seen:
                array[j] =False


            elif temp[1] in dic and temp[0] in dic[temp[1]] and temp[2] in dic[temp[1]] and\
                    temp[1] in seen:
                array[j] =False



            elif temp[0] in dic and temp[2] in dic and\
                    temp[1] in dic[temp[0]] and\
                    temp[1] in dic[temp[2]] and neighbor_checking(dic,temp[1],seen):
                array[j]=False


            else:
                continue
        s = 0
        for k in range(len(array)):
            if array[k]==True:
                s+=1
        if s == len(array):
            print("active")
        else:
            print("inactive")
