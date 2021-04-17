import numpy as np
import math

# Term Frequency Inverse Document Frequency

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

# distance function
def getDist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)

def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=float)
    for i, vector in enumerate(data):
      for j, compareVector in enumerate(data):
        if i == j:
          dist[i][j] = np.Inf
        else:
          dist[i][j] = getDist(vector, compareVector)

    return np.unravel_index(np.argmin(dist), dist.shape)

def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal
    # despite casing) can be done with
    docs = [line.lower().split() for line in text.split('\n')]
    words = [item for sublist in docs for item in sublist]
    unique = set(words)

    # 2. go over each unique word and calculate its term frequency, and its document frequency
    tfidf = dict()
    for word in unique:
        tfv = [line.count(word) / len(line) for line in docs]
        df = words.count(word) / len(docs)
        tfidf[word] = [tf * math.log(1 / df, 10) for tf in tfv]

    # 3. after you have your term frequencies and document frequencies, go over each line in the text and
    # calculate its TF-IDF representation, which will be a vector
    line_tfidf = list()
    for i, line in enumerate(docs):
        line_tfidf.append([tfidf[word][i] for word in line])

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.
    nearest = find_nearest_pair(line_tfidf)
    print(nearest)

main(text)