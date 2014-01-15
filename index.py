#! /usr/bin/env python

from nltk import tokenize
import sys

# Read file
def file2shingles(path='big.txt', size=1):
    f = open(path, 'r')
    file_string = f.read()
    token_list = tokenize.word_tokenize(file_string)
    return [' '.join(s).lower() for s in shingle(token_list, size)]

# Make shingles
def shingle(token_list, size):
    shingles = set()
    for i in range(0, len(token_list)-size+1):
        yield token_list[i:i+size]

# Count occurrences of following link
def link_count(shingle_list):
    # Initialize output dict
    link_dict = {}
    # iterate through list of links
    for i in range(len(shingle_list) - 1):
        # see if there's an entry for this link
        entry = link_dict.get(shingle_list[i])
        current_link = shingle_list[i]
        next_link = shingle_list[i + 1]
        if (entry):
            # Check to see if following link has been counted already
            next_link_entry = entry.get(next_link)
            if (next_link_entry):
                # Calculate probabilities instead of just word count ?
                link_dict[current_link][next_link] += 1
            else:
                link_dict[current_link][next_link] = 1
        else:
            link_dict[current_link] = {str(next_link): 1}
    return link_dict

""" Establishes a baseline probability distribution based on an input file or stream """
class BaselineProbability(object):
    def __init__(self,path='big.txt', size=1): 
        self.path = path
        self.shingle_size = size
        shingle_list = file2shingles()
        self.link_count_dict = link_count(shingle_list)

    def degree_of_freedom(self, limit):
        """ Return a list of words from corpus, ordered (descending) by degrees of freedom, up to the limit """
        return sorted(self.link_count_dict, key=lambda x: len(self.link_count_dict[x].values()), reverse=True)[:limit]



    


