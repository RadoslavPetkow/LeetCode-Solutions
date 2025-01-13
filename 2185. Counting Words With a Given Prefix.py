words = ["leetcode","win","loops","success"]
pref = "code"

result = 0

for i in words:
    if i.startswith(pref):
        result+=1

print(result)