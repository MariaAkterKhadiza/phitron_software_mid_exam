def maxBalanceSting(s):
    if not s:
        return 0
    balance = 0
    start = 0
    substring = []


    for i,char in enumerate(s):
        if char == 'R':
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            substring.append(s[start:i+1])
            start = i + 1
   
    return substring
s = input()
result = maxBalanceSting(s)
number_substr = len(result)
print(number_substr)
for substr in result:
    print(substr)