"""
Problem 2:

Chit Chat Application - Function:

(b) How one can check if the restriction is on a number of words rather than letters?
Write a function that allows a message with only 30 words.
"""
n=str(input())
def mess_word(n):
    word=n.split()
    if len(word) <= 30:
        return n
    else:
        return (" ".join(word[:30]))
print(mess_word(n))
