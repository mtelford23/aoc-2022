import collections

file = "day12/day12-test.txt"

with open(file) as f:
    landscape = [line.strip() for line in f.readlines()]

sCoords = (999, 999)
eCoords = (999, 999)

dirs = [(-1,0), (0,1), (1,0), (0,-1)] #U, R, D, L

for r, line in enumerate(landscape):
    if 'S' in line:
        c = line.index('S')
        sCoords = (r, c)

    if 'E' in line:
        c = line.index('E')
        eCoords = (r, c)


def bfs(graph, root):

    visited = set() 
    q = collections.deque([root])
    visited.add(root)
    path = []

    while q:
        # Dequeue a vertex from queue
        path.append(q.popleft())
        #print(path[-1], type(path[-1]))
        q.clear() #misplaced i think

        cr, cc = path[-1]
        
        for dr, dc in dirs:
            nr = dr + cr
            nc = dc + cc

            if nr < len(graph) and nc < len(graph[0]) and nr >= 0 and nc >= 0:

                if graph[cr][cc] == 'S' and (graph[nr][nc] == 'a' or graph[nr][nc] == 'b'):
                    visited.add((nr,nc))
                    q.append((nr, nc))

                if (nr,nc) is eCoords and (graph[cr][cc] == 'z' or graph[cr][cc] == 'y'):
                    print(len(path))
                    break

                elif ord(graph[cr][cc]) + 1 == ord(graph[nr][nc]) or ord(graph[nr][nc]) <= ord(graph[cr][cc]):
                    if (nr, nc) not in visited and graph[nr][nc] != 'E':
                        visited.add((nr,nc))
                        q.append((nr, nc))
                            
    
        # if len(path) == 20:
        #     pass
        # print(len(path))

bfs(landscape, sCoords)


