#!/usr/bin/env python
# coding: utf-8

# The following function freq_histogram receives a dictionary word_freqs, and returns a histogram for word frequencies. A histogram is a list of integers, where the value at each index is the number of words in word_freqs whose frequency is equal to that index.
# 
# For example, the histogram [1,5,0,2] means that word_freqs contains one word with the frequency of 0, five words with a frequency of 1, no words with a frequency of 2 and two words with a frequency of 3:
# 
# For example,
# 
# freq_histogram({'absurd': 0, 'thought': 2, 'wood': 1, 'one': 2,'tree':1}) returns [1,2,2]

# In[79]:


def freq_histogram(word_freqs):
    freq_list = list(word_freqs.values())
    freq_list.sort()
    order_list = list(range(max(word_freqs.values())+1))
    freq_hist = [0]*len(order_list)
    print(f'sorted freq_list \n{freq_list}\n')
    #print(f'freq_hist = {freq_hist}')
    print(order_list)
    #print()
    
    for i in order_list:
        index = i
        #print(f'i = {i}')
        count = freq_list.count(index)
        #print(f'index = {index} - count = {count}')
        freq_hist[index] = count
        #print(f'{freq_hist}')
        #print('--------------------------------------------------')
    return freq_hist
#word_freqs = {'absurd': 0, 'thought': 2, 'wood': 1, 'one': 2, 'tree': 1}
#word_freqs = {'absurd': 1, 'thought': 1, 'wood': 1, 'one': 2, 'tree': 5, 'absurd2': 6, 'thought2': 4, 'wood2': 1, 'one2': 3, 'tree2': 10}
#word_freqs = {'absurd': 10}
print(freq_histogram(word_freqs))


# In[ ]:




