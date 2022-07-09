# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

'''
Make sure to answer the following questions about your coding process:

How does this solution ensure data immutability?
there is no inputs changed

Is this solution a pure function? Why or why not?
yes it is because the inout was stored in an array but also returned it as sorted.

Is this solution a higher order function? Why or why not?
no because there is no arguments passing along.

Would it have been easier to solve this problem using a different programming style?
no

Why in particular is functional programming a helpful paradigm when solving this problem?
Because we dont need to create that many classes/objects to solve this problem. We can just wrute this code simple.

'''
