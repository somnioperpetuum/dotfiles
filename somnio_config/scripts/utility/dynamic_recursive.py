import numpy as np
import math


prob = []
word_dict = {}
counter = 0



def rec_helper(vector,column_length):
     '''
     Recursion helper of vec_to_matrix

     param::vector -> np.array
     param::column_length -> (natural,natural)

     returns ->  2d array
     '''
     global matrix
     matrix = np.append(matrix,vector)
     if column_length <= 0:
         return matrix
     return rec_helper(vector,column_length-1)

def vec_to_matrix(grid_size):
    '''
    Takes a tuple of two naturals and returns a matrix

    param::grid_size -> (x-axis,y-axis)

    returns -> 2d array
    '''
    global matrix
    matrix = np.array([])
    column_length = grid_size[1]
    vector = np.array([0 for x in range(0,grid_size[0])])
    matrix = rec_helper(vector,column_length - 1)
    return np.reshape(matrix,(grid_size[1],grid_size[0]))


def common_longest_substring(word,possible_word):
    '''
    Takes a word and finds the common longest substring usisng dynamic programming
   
    param::word -> string
    param::word -> string

    returns -> int
    '''
    matrix = vec_to_matrix((len(possible_word),len(word)))
    for index,letter in enumerate(word):
        for jndex, possible_letter in enumerate(possible_word):
            if letter == possible_letter:
                matrix[index][jndex] = matrix[index - 1][jndex - 1 ] + 1
            else:
                matrix[index][jndex] = max(int(matrix[index-1][jndex]),int(matrix[index][jndex-1]))
    return matrix[-1][-1]



def best_suggestions(word):
    # Finding the coommon longets substring in the dict
    word = word.lower()
    for item,index in word_dict.items():
         prob.append((index,item,common_longest_substring(word,item)))
    suggestions = [item for x,item,value in prob if value > math.ceil((len(word))* .55)]
    for item in suggestions:
        if word == item:
            return item
    return suggestions



# Here is the code that you should place to retrieve the info form the database as a word_list
# So the next code is a placeholder.




word_list = [
    "linux","container"
]

# Set creation for eliminating duplicates and setting them to lower
word_set = set([x.lower() for x in word_list])

# Dictionary creation 
for item in word_set:
    word_dict[item] = counter
    counter += 1 


print(best_suggestions("cont"))
