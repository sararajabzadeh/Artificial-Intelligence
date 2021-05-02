import copy , heapq
def heuristic(matrix):
    hValue=0
    n = len(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            indexi = (int(matrix[i][j])-1)//n
            indexj = (int(matrix[i][j])-1)%n
            if i != indexi:
                hValue+=1
            if j!= indexj:
                hValue+=1
    return hValue

def rotateRight(array):
    return array[-1:] + array[:-1]
def rotateLeft(array):
    return array[1:] + array[:1]

n = int(input())
firstState = []
for i in range(n):
    firstState+=[input().split()]

if heuristic(firstState)==0:
    print(0)
else:
    prime = [False]*90439
    frontier = []
    # seen = [firstState]
    heapq.heappush(frontier,(heuristic(firstState),firstState,0))
    hale = False
    # x=0
    while hale==False:
    # while x<8:
    #     x+=1
        # print("x:",x)
        temp = heapq.heappop(frontier)
        hash = 0
        for i in range(n):
            matrix = copy.deepcopy(temp[1])
            queue = rotateRight(temp[1][i])
            matrix[i] = queue
            for j in range(n):
                hash += ((hash+int(matrix[i][j]))*100)%90439
            hash = hash%90439
            # prime[hash] = True
            # if matrix not in seen:
            if prime[hash]==False:
                heapq.heappush(frontier,(heuristic(matrix)+(temp[2]+1)*n,matrix,temp[2]+1))
                # seen.append(matrix)
                prime[hash]=True
            if heuristic(matrix)==0:
                hale = True
                break
        if hale==False:
            hash = 0
            for i in range(n):
                matrix = copy.deepcopy(temp[1])
                queue = rotateLeft(temp[1][i])
                matrix[i] = queue
                for j in range(n):
                    hash += ((hash + int(matrix[i][j])) * 100) % 90439
                hash = hash%90439
                # if matrix not in seen:
                if prime[hash]==False:
                    # seen.append(matrix)
                    prime[hash]=True
                    heapq.heappush(frontier,(heuristic(matrix)+(temp[2]+1)*n,matrix,temp[2]+1))
                if heuristic(matrix)==0:
                    # print("salam")
                    hale = True
                    break
            if hale==False:        # print(matrix)
                array=[]
                for i in range(n):
                    matrix = copy.deepcopy(temp[1])
                    array = []
                    for j in range(n):
                        array += [temp[1][j][i]]
                    queue = rotateLeft(array)
                    for j in range(n):
                        matrix[j][i] = queue[j]
                    for j in range(n):
                        hash += ((hash + int(matrix[i][j])) * 100) % 90439
                    hash = hash%90439
                    # if matrix not in seen:
                    if prime[hash]==False:
                        heapq.heappush(frontier,(heuristic(matrix)+(temp[2]+1)*n,matrix,temp[2]+1))
                        # seen.append(matrix)
                        prime[hash]=True
                    if heuristic(matrix)==0:
                        hale=True
                        break
                if hale==False:
                    array=[]
                    for i in range(n):
                        matrix = copy.deepcopy(temp[1])
                        array = []
                        for j in range(n):
                            array += [temp[1][j][i]]
                        queue = rotateRight(array)
                        for j in range(n):
                            matrix[j][i] = queue[j]
                        for j in range(n):
                            hash += ((hash + int(matrix[i][j])) * 100) % 90439
                        hash=hash%90439
                        # if matrix not in seen:
                        if prime[hash]==False:
                            heapq.heappush(frontier, (heuristic(matrix)+(temp[2]+1)*n, matrix, temp[2] + 1))
                            # seen.append(matrix)
                            prime[hash]=True
                        if heuristic(matrix)==0:
                            hale=True
                            break
                        # print(matrix)
                    # print("sallllam")
    print(temp[2]+1)