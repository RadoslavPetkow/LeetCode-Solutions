words = ["mass","as","hero","superhero"]
result = []
for i in words:
    for j in words:
        if j != i and j.find(i) != -1:
            result.append(i)

print(list(set(result)))

"""
CHATGPT SOLVE
def string_matching(words):
    # Sort words by length: shorter words come first
    words.sort(key=len)
    result = []

    for i in range(len(words)):
        for j in range(i+1, len(words)):
            # If words[i] is a substring of words[j], add to result and move on
            if words[i] in words[j]:
                result.append(words[i])
                break

    return result
"""