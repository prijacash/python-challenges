# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# def alphabetize(string):
#     new_list = list(string)
#     new_list.sort()

#     new_string = ""
#     for letter in new_list:
#         new_string = new_string + letter
#     return new_string

# print(alphabetize("supercalifragilisticexpialidocious"))

word = "supercalifragilisticexpialidocious"

#conver string to list
word_li = list(word)

# sort list
word_li.sort()

# convert list to string
new_string = ''
for char in word_li:
    new_string += char

print(new_string)
# print(dir(list))

# my_li