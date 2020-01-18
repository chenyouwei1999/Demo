# https://codeshare.io/GkM6eM
# dvd
k = int(input())
for _ in range(k):
    n = int(input())
    dvds = list(map(int, input().split()))
    current = 1
    for i in range(n):
        if dvds[i] == current:
            current += 1
    print(n - current + 1)
