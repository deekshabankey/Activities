"""
Problem - I 

sentence = "Hey I am walking here I am walking here o captain my captain water water everywhere nor a drop to drik"
print(verse, "\n")

# split sentence into list of words
sentence_list =  # You will have to fill out the function 
print(sentence_list, '\n')

# convert list to set to get unique words
sentence_set = 
print(sentence_set, '\n')

# print the number of unique words
num_unique = 
print(num_unique, '\n')
"""

sentence= "Hey I am walking here I am walking here o captain my captain water water everywhere nor a drop to drink"
s_l=sentence.split()
print("reverse= "," ".join(s_l[::-1]))
print("sentence_list= ",s_l,"\n")

s_s=set(s_l)
print("sentence_set= ",s_s,"\n")

print("num_unique: ",len(s_s),"\n")
