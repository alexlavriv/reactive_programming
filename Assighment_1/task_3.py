
def ngrams(n, words):
    for w_count in range(len(words) - n):
        res = []
        for t in range(n):
            res.append(words[w_count+t])
        yield res
sentence = "The fat red fox jumped over the crazy black dog"
for x in ngrams(3,sentence.split()): print (x)