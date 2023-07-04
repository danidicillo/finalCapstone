# T21 - COMPULSORY TASK 1:

# 1) Create a ﬁle called semantic.py and run all the code extracts above.

print("COMPULSORY TASK 1: \n")

#   SIMILARITY WITH SPACY: 
print("SIMILARITY WITH SPACY: \n")

import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print("SIMILARITY BETWEEN WORD1 AND WORD2: ", word1.similarity(word2))
print("SIMILARITY BETWEEN WORD3 AND WORD2: ", word3.similarity(word2))
print("SIMILARITY BETWEEN WORD3 AND WORD1: ", word3.similarity(word1))

print(" \n")

#   WORKING WITH VECTORS: 

print("WORKING WITH VECTORS: \n")

tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print(" \n")

#   WORKING WITH SENTENCES: 

print("WORKING WITH SENTENCES: \n")
sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

print(" \n")

# 2) Write a note about what you found interesting about the similarities between cat, monkey and banana and think of an example of your own:

#   SIMILARITY WITH SPACY: 
# It is interesting to see that "monkey" has a higher score of similarity to "cat" than to "banana". This is happening because spaCy is considering first the category of "animal"
# to compare all the words. Then, it uses the frequent association between the two animals and the fruit finding that monkey has a higher association with banana than cat. So, this
# way it finds that monkey is more similar to cat than to banana, and that banana is more similar to monkey than to cat.

# An example of my own could be as follows:
# EXAMPLE 1:
print("AN EXAMPLE OF MY OWN FOR SIMILARITY BETWEEN TWO WORDS: \n")

word1 = nlp("dog")
word2 = nlp("rabbit")
word3 = nlp("carrot")

print("Similarity between dog and rabbit: ", word1.similarity(word2))
print("Similarity between carrot and rabbit: ", word3.similarity(word2))
print("Similarity between carrot and dog: ", word3.similarity(word1))

print(" \n")

# EXAMPLE 2:
print("AN EXAMPLE OF MY OWN FOR SIMILARITY AMONG MULTIPLE WORDS (WORKING WITH VECTORS): \n")

tokens = nlp('BMW F-35 Spitfire Bentley ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print(" \n")

# 3) Run the example file with the simpler language model "en_core_web_sm" and write a note on what you notice is different from the model "en_core_web_md":

# We can see that the model's efficiency is lower for the "en_core_web_sm" compared to the "en_core_web_md". We see that the scores for every similarity comparison get reduced values.
# This is happening because "the model used" for this part of the task "has no word vectors loaded, so the result of the doc.similarity method will be
# based on the tagger, parser, and NER, which may not give useful similarity judgements".

# Quoted from "UserWarning: [W007] got after running the example.py code.