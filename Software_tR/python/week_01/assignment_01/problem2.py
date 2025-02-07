from collections import Counter
def minRemovalsToGoodSequence(a):
    freq = Counter(a)
    removals = 0
   
    for x, count in freq.items():
        if count > x:
            removals += count - x
        elif count < x:
            removals += count
   
    return removals




n = int(input())
a = list(map(int, input().split()))


result = minRemovalsToGoodSequence(a)


print(result)