#!python 3
#madlibs.py - A Mad Libs program by John Gummels

import random, re

adj = []
nou = []
adv = []
ver = []

t = 0
x = 0
y = 0
z = 0

# Select random sentence.
choice = random.choice(open('sentences.txt').readlines())



#Fill words with user input. 
for word in choice.split():
    if re.search('ADJECTIVE?', word):
        adj.append(input('Enter adjective: ')) 
        choice = re.sub("ADJECTIVE", adj[x], choice, 1)
        x += 1
    elif re.search('NOUN?', word):
        nou.append(input('Enter noun: '))
        choice = re.sub("NOUN", nou[y], choice, 1)
        y += 1
    elif re.search('ADVERB?', word):
        adv.append(input('Enter adverb: '))
        choice = re.sub("ADVERB", adv[z], choice, 1)
        z += 1
    elif re.search('VERB?', word):
        ver.append(input('Enter verb: '))
        choice = re.sub("VERB", ver[t], choice, 1)
        t += 1    

#TODO: print Mad Lib and save to text file. 
madlibs = open("madlibs.txt", 'a')
madlibs.write(choice + "\n")
madlibs.close
print(choice)
