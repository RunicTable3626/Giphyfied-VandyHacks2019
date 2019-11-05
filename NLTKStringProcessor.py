import nltk
import spacy
import pprint

##nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
##
##def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
##    """https://spacy.io/api/annotation"""
##    texts_out = []
##    for sent in texts:
##        doc = nlp(" ".join(sent)) 
##        texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
##    return texts_out


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def stopword_remover(text_sentence):
    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(text_sentence)

    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    return filtered_sentence

def pos_filter(word_list):
    tagged = nltk.pos_tag(word_list)
    return tagged

##def pos_priority_filter(word_list):
##    priority_dict = { 1:
##                      2:
##                      3:
##                      4:
##                      5
    
 
file = open('Lyrics\Lalala.txt','r')
lyric_text = file.read()
lyric_text = lyric_text.splitlines()
tokenized_text = []
for line in lyric_text:
    tokenized_text.append(pos_filter(stopword_remover(line)))
pprint.pprint(tokenized_text)



