
# coding: utf-8

# In[1]:

def word_distribution(word):
    '''This function will take some user input(sentences), strip functions and provide a dictionar
    for word count'''
    import string
    word_dict=dict()
    
    word= word.lower()
    word_list=[x.strip(string.punctuation) for x in word.split()]#generate a list of words with stripped punctuation
    
    for item in word_list:
        if item in word_dict: #if key of dict is already there, then add one to count
            word_dict[item]+=1
        else:
            word_dict[item]=1 # if the key is not in the dict, start the count
    return word_dict


# In[2]:

user_input=input('whats your sentence? lets count your words \n')
word_distribution(user_input)





