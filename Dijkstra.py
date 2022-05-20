from queue import PriorityQueue


def Dijkstra(start, stop, G):
    dist = [float('inf')]*len(G)
    #-1 oznacza ze brak poprzednika
    prev = [-1]*len(G)
    visited=[0]*len(G)
    #wierzcholki liczymy od zera
    dist[start] = 0
    prev[start] = -1
    H = PriorityQueue()
    H.put((0, start))
    while not H.empty():
        (u_dist, u) = H.get()
        #usuwam elementy ktore juz byly odwiedzone w kolejce
        while not H.empty():
            if visited[u] == 0:
                break
            (u_dist, u) = H.get()
        visited[u]=1
        for i in range(0, len(G)):
            #przy zalozeniu ze nie ma krawedzi o wadze 0, 0 traktuje jako brak krawedzi
            if visited[i]==0:
                if G[u][i]!=0:
                    if (dist[i] > (dist[u] + G[u][i])):
                        dist[i] = dist[u] + G[u][i]
                        prev[i] = u
                        H.put((dist[i], i))
        tmp = prev[stop]
        kolejnosc = []
        kolejnosc.append(stop)
        kolejnosc.append(tmp)
        for i in range(2, len(prev)):
            tmp = prev[tmp]
            if tmp == -1:
                break
            kolejnosc.append(tmp)
    print(dist)
    print(prev)
    kolejnosc.reverse()
    return kolejnosc


print("Przykład 1")
G=[
    [0,2,1,7,0,3],
    [2,0,0,6,4,9],
    [1,0,0,3,0,0],
    [7,6,3,0,1,0],
    [0,4,0,1,0,0],
    [3,9,0,0,0,0]
   ]
print(Dijkstra(5,2,G))
G1=[
    [0,1,0,0,4,8,0,0],
    [0,0,2,0,0,6,6,0],
    [0,0,0,1,0,0,2,0],
    [0,0,0,0,0,0,1,4],
    [0,0,0,0,0,5,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,1],
    [0,0,0,0,0,0,0,0]
   ]
print("Przykład 2")
print(Dijkstra(0,7,G1))

g2 = [
    [0, 5, 7, 4],
    [5, 0, 1, 2],
    [7, 1, 0, 0],
    [4, 2, 0, 0]
]
print("Przykład 3")
print(Dijkstra(0, 2, g2))