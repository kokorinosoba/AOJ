from collections import deque
n, q = map(int, input().split())
L = [deque() for _ in range(n)]
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        L[query[1]].append(query[2])
    elif len(L[query[1]]) > 0:
        if query[0] == 1:
            print(max(L[query[1]]))
        elif query[0] == 2:
            L[query[1]].remove(max(L[query[1]]))