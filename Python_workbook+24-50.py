
# coding: utf-8

# ### The Python Workbook: Solve 100 Exercises
# ### EX 24-50
# #### A Udemy course to practice python with the given ex. some of the exercises are not included as they can be easliy done mentall

# In[ ]:

# Python workbook ex. from UDEMY


# In[11]:

#ex 24
d= dict(a=list(range(1,11)),b=list(range(11,21)),c=list(range(21,31)))
for key, value in d.items(): #iteration over a dictionary
    print(key,'has value', value)
    


# In[12]:

"""ex. 25 Cistern LeverMake a script that prints out letters of English alphabet from a to z, one letter per line in the terminal.
"""
# Method 1
alphabet_letters='abcdefghijklmnopqrstuvwxyz'
for letter in alphabet_letters:
    print(letter)
# method 2
import string
for letter in string.ascii_lowercase:
    print(letter)


# In[13]:

#ex 26  Make a script that prints out numbers from 1 to 10
for number in range(1,11):
    print (number)


# In[17]:

# ex 27. 
'''Create a function that calculates acceleration given initial velocity v1,
final velocity v2, start time t1, and end time t2. The formula for acceleration
is:
a=(v2-v1)/(t2-t1)

To test your solution, call the function by inputting values 0, 10, 0, 20 for v1, v2, t1, and t2 respectively, and you should get the expected output.'''
def acceleration_calc(v1,v2,t1,t2):
    acceleration=(v2-v1)/(t2-t1)
    return acceleration
print (acceleration_calc(0,10,0,20))


# In[19]:

#ex 29
'''Please write a function that calculates liquid volume in a sphere using
the following formula.
The radius r  is always 10, so consider making it a default parameter.'''
def liquid_volume(h,r=10): #r will default to 10 if no input
    import math
    
    volume=(4*math.pi*(r**3)/3)-(math.pi*(h**2)*((3*r)-h))/3
    return volume
print (liquid_volume(2))


# In[20]:

c=1
def foo():
    return c
c=3
print(foo())


# In[24]:

# ex 35. Create a function that takes any string as input
#and returns the number of words for that string.
def word_count(sentence):
    list_of_words=sentence.split(' ')
    return len(list_of_words)


# In[25]:

word_count('Hi my name is')


# In[36]:

#ex 36 
"""Please download the words1.txt file from the attachment and then
create a Python function that takes a text file as input and returns the number
of words contained in the text file."""
def text_count():
    word_list=[]
    with open('words1.txt','r') as f:
        words=f.read()
        word_list=words.split(' ')
    return len(word_list)


# In[37]:

text_count()


# In[49]:

#ex 37 Method 1
"""Create a function that takes a text file as input and returns the number
of words contained in the text file. Please take into consideration
that some words can be separated by a comma with no space. For example
"Hi,it's me." would need to be counted as three words. For your convenience, 
you can use the text file in the attachment."""
def text_count2():
    with open('words2.txt','r') as file:
        text=file.read()
        text.replace(',',' ')
        word_count=text.replace(',',' ').split(' ')
        return len(word_count)
    


# In[50]:

text_count2()


# In[51]:

#ex 37 Method 2: Using regular expressions
import re
def count_words_re(filepath):
    with open(filepath,'r') as file:
        words=file.read()
        words_list=re.split(',| ', words) # replacing commas with space using regex
        return len(words_list)


# In[52]:

count_words_re('words2.txt')


# In[53]:

import math
dir(math)


# In[56]:

# ex 41
import string
with open('words33.txt','w') as file:
    for letter in string.ascii_lowercase: # using string library for lower ccase
        file.write(letter + '\n')# adding letter and start a new line. 


# In[60]:

#ex 42 Print out in each line the sum of homologous items of the two sequences.
a=[1,2,3]
b=(4,5,6)
for i,j in zip(a,b):
    print(i+j)


# In[64]:

#ex 43
"""write to a file so that two letters each line"""
import string
with open('two_letters.txt','w') as file:
    for letter1, letter2 in zip(string.ascii_lowercase[0::2],string.ascii_lowercase[1::2]):
    #The first [0::2] starts from a and skips b to c and so on
    #the second [1::2] starts from b and skips to d and so on
    #zip function concats the two together: so letter1=a,letter2=b zip(letter1,letter2)=ab 
        file.write(letter1+letter2 +'\n')


# In[71]:

#ex 44
'''write to a file so that three letters per line'''
import string
letters=string.ascii_lowercase+ ' ' #adding space so that it adds up to 27. otherwise iteration will stop short without printing y,z 
with open('three_letters.txt','w') as file:
    #slice of threes
    for l1,l2,l3 in zip(letters[0::3],letters[1::3],letters[2::3]):
        file.write(l1+l2+l3+'\n')
    


# In[72]:

print(string.ascii_lowercase[0::3])
print (string.ascii_lowercase[1::3])
print(string.ascii_lowercase[2::3])


# In[84]:

#ex 45 write a file for each letter
import string
for letter in string.ascii_lowercase:
    with open('letter_folder/'+letter+'.txt','w') as file:#open a new folder
        #name each folder by its letter
        file.write(letter+'\n')
        
# Another method to create a non existing file
import os 
if not os.path.exists('letters'):
    os.makedirs('letters')
        


# In[92]:

#EX 46 Method1 
#write a script the extract letters from the previous 26 files to a list
letter_list=[]

for letter in string.ascii_lowercase:
    with open('letter_folder/'+letter+'.txt','r') as file:
        each_letter=file.read()
    letter_list.append(each_letter.rstrip('\n'))


# In[93]:

print(letter_list)


# In[96]:

#EX 45 Method 2
import glob
letters=[]
file_list=glob.glob('letter_folder/*.txt')#to find all the files that match given patters
for filename in file_list:
    with open(filename,'r') as file:
        letters.append(file.read().rstrip('\n'))
print(letters)


# In[103]:

#EX 47 iterate over files from previous example. if letter is in string'python' add it to list
import glob
l_in_python=[]
file_list=glob.glob('letter_folder/*.txt')
for filename in file_list:
    with open(filename,'r') as file:
        letter=file.read().rstrip('\n')
    if letter in 'python':
        l_in_python.append(letter)
print(l_in_python)


# In[ ]:



