from collections import defaultdict
def wordcount(body):
    counts = defaultdict(int)
    for word in body.split():
        counts[word] += 1
    return counts
