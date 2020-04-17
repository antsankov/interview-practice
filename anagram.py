# Given an array of words, print the count of all anagrams together in sorted order (increasing order of counts).
# For example, if the given array is {"cat", "dog", "tac", "god", "act"}, then grouped anagrams are "(dog, god) (cat, tac, act)". So the output will be 2 3.

def anagrams(grams):
    counts = {}
    for gram in grams:
        s = "".join(sorted(gram))
        if s in counts:
            counts[s] += 1
        else:
            counts[s] = 1

    print(counts)
        
anagrams(["cat", "dog", "tac", "god", "act"])