from collections import deque as d

def Solution(num, a, b, s):
    if a == b: return 0
    q, v = d([(a, 0)]), {a}
    while q:
        idx, j = q.popleft()
        for step in [(idx + s[idx - 1]) % num, (idx - s[idx - 1]) % num]:
            if step == b: return j + 1
            if step not in v:
                v.add(step)
    return -1


num = int(input())
a = int(input())
b = int(input())
arr = []
for _ in range(num):
    arr.append(int(input()))

print(Solution(num, a, b, arr))