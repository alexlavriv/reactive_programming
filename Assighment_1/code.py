# P1.1
# P1.1: [0, 1, 2, 3] -> [1, 3, 5, 7]
def p_1_lc(inputlist):
    [inputlist[i]+i+1 for i in range(len(inputlist))]

# P1.2
# [3, 5, 9, 8] -> [True, False, True, False]
def p_2_lc(inputlist):
    return [k%3==0 for k in inputlist]

def p_2_fo(inputlist):
    return list(map(lambda x: x%3==0, inputlist))

# P1.3
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] -> [0, 1, 4, 9, …, 81]
def p_3_lc(inputlist):
    return [k**2 for k in inputlist]

def p_3_fo(inputlist):
    return list(map(lambda x: x**2, inputlist))
# P1.4
# P1.4: [“apple”, “orange”, “pear”] -> [“A”, “O”, “P”]
def p_4_lc(inputlist):
    return k[0].upper() for k in inputlist]

def p_4_lc (inputlist):
    return list(map(lambda x: x[0].upper(), inputlist))
# P1.5
# [“apple”, “orange”, “pear”] -> [“apple”, “pear”]
def p_5_lc(inputlist):
  return 0

# P1.6 
# [“apple”, “orange”, “pear”] -> [(“apple”, 5), (“orange”, 6), (“pear”, 4)]
def p_6_lc(inputlist):
    return [(k,len(k)) for k in inputlist]

def p_6_fo(inputlist):
    return list(map(lambda x: (x,len(x)), inputlist))
# P1.7 
# [0, 1, 2, 3, 4, 5, 6, 8] -> [1, 3, 5]
def p_7_lc(inputlist):
    return [t for t in inputlist if t%2==1]

def p_7_fo(inputlist):
    return list(filter(lambda x: x%2==1, inputlist))

# P1.8: 
# [1, 2, 4, 5, 7] -> [1, 4, 7] {hint: indexes}
def p_8_lc(inputlist):
    [k[i] for i in range(len(inputlist)) if i % 2 == 0]

def p_8_fo(inputlist):
    