#Giancarlo Sirio
#Markov Model Class

import math


def clean_text(txt):
    """inputs a string of text as a parameter
       returns a list of containing words that have been cleaned 
    """
    txt = txt.lower()
    txt = txt.replace(',','')
    txt = txt.replace('.','')
    txt = txt.replace('?','')
    txt = txt.replace('!','')
    txt = txt.replace('"','')
    txt = txt.replace(';','')
    txt = txt.replace(':','')
    txt = txt.split()
    return txt

def stem(s):

    """inputs a string and returns the stem of the word
    """
    if s[-3:] == 'ing' and len(s) > 4:
        if s[-4] == s[-5]:
            s = s[:-4]
        else:
            s = s[:-3]
    elif s[:3] == 'mis' or s[:3] == 'non' or s[:3] == 'pre' or s[:3] == 'tri' or s[:3]=='uni':
        if s[3] == '-' :
            s = s[4:]
        else:
            s = s[3:]
    elif s[:2] == 'ex' or s[:2] == 'co' or s[:2] == 'de' or s[:2] == 'il' or s[:2]=='im' or s[:2]=='in' or s[:2]=='ir' or s[:2]== 'un' and len(s) > 5:
            s = s[2:]
    elif s[:4] == 'ante' or s[:4] == 'anti' or s[:4] == 'semi' or s[:4] == 'fore' or s[:4] == 'homo' or s[:4] == 'mono' or s[:4]=='post' or s[:4] == 'para':
        if s[4] == '-':
            s = s[5:]
        else:
            s = s[4:]
    elif s[-2:] == 'er' and len(s) > 4:
        if s[-3] == s[-4]:
            s = s[:-3]
        else:
            s = s[:-2]
    elif s[-1] == 's':

        stem_rest = stem(s[:-1])
        return stem_rest
    
    elif s[-3:] == 'ies'  or s[-3:] == 'ier' and len(s) > 4:
        if len(s) <= 4:
            s = s[:-1]
        else:
            s = s[:2]

    elif s[-1] == 'y':
        s = s[:-1]
        s += 'i'
        

    return s
        
        
def sentence_lengths(s):
    """inputs a string s, returns a list with all the lengths of sentences
    """
    s = s.replace('!','.')
    s = s.replace('?','.')
    s = s.replace(';','.')
    s = s.replace('"','')
    s = s.replace("'",'')
    s = s.split('.')
    s = s[:-1]
    sen_len = []
    for i in range(len(s)):
        s[i] = s[i].split(' ')
    for i in range(1,len(s)):
        s[i] = s[i][1:]
    for i in range(len(s)):
        sen_len += [len(s[i])]
    return sen_len

def four_grams(txt):
    """inputs a string of text
        returns a list of all four character combinations
    """
    txt = txt.lower()
    txt = txt.replace(',','')
    txt = txt.replace('.','')
    txt = txt.replace('?','')
    txt = txt.replace('!','')
    txt = txt.replace('"','')
    txt = txt.replace(';','')
    txt = txt.replace(':','')
    
    list_grams = []
    for i in range(len(txt) - 3):
        list_grams += [txt[i:i+4]]
        
    return list_grams
        
        
def compare_dictionaries(d1,d2):
    """inputs two dictionaries
       returns their log similarity scores
    """
    score = 0
    total_words1 = 0
    for key in d1:      #gets the total number of times a word appears in the dict
        total_words1 += d1[key]

    for key in d2:
        if key in d1:
            score += d2[key]* math.log(d1[key]/total_words1)
        else:
            score += d2[key] * math.log(.5/total_words1)
    
    return score    

class TextModel:
    def __init__(self,model_name):
        """constructor function for TextModel Object
        """
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.four_grams = {}
        

    def __repr__(self):
        """String representation of the TextModel object
        """
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of four-adjacent characters: ' + str(len(self.four_grams)) 
        return s

    def add_string(self,s):
        """adds a string of text s to the model
        """
        #creates a dictionay of the frequency of sentence lengths
        sen_len_list = sentence_lengths(s)
        for x in sen_len_list:
            if x not in self.sentence_lengths:
                self.sentence_lengths[x] = 1
            else:
                self.sentence_lengths[x] += 1


        #creates a list of all the words in the text
        word_list = clean_text(s)
        
        #creates a dictionary with all the number of times a word appears in text
        for w in word_list:
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1

        #creates a list of word lengths       
        list_wordlengths = [len(x) for x in word_list]
        
        #creates a dictionary of the frequency of word lengths
        for x in list_wordlengths:
            if x not in self.word_lengths:
                self.word_lengths[x]= 1
            else:
                self.word_lengths[x] += 1
        #creates a list of all the stems of words in a text
        list_stems = [stem(w) for w in word_list]
        #creates a dictionary of all the frequency of stems in the word_list
        for x in list_stems:
            if x not in self.stems:
                self.stems[x] = 1
            else:
                self.stems[x] += 1

        list_grams = four_grams(s)
        #creates a dictionary of all the frequency of four character strings in the string
        for x in list_grams:
            if x not in self.four_grams:
                self.four_grams[x] = 1
            else:
                self.four_grams[x] += 1
    
    def add_file(self,filename):
        """adds a file of text to an existing filename
        """
        f = open(filename,'r',encoding='utf8', errors = 'ignore')
        text = f.read()
        f.close()
        self.add_string(text)

    def save_model(self):
        """saves the dictionaries for the Text model object onto a text file
        """
        #saves model for word frequencies dictionary
        d = self.words
        f = open(str(self.name)+ '_words.txt' , 'w')
        f.write(str(d))
        f.close
        #save model for word lengths dictionary
        d = self.word_lengths
        f = open(str(self.name)+'_word_lengths.txt','w')
        f.write(str(d))
        f.close
        #save model for stems dictionary
        d = self.stems
        f = open(str(self.name)+ '_stems.txt','w')
        f.write(str(d))
        f.close
        #save model for sentence lengths dictionary
        d = self.sentence_lengths
        f = open(str(self.name)+ '_sentence_lengths.txt','w')
        f.write(str(d))
        f.close
        #save model for four adjacent characters dictionary
        d = self.four_grams
        f = open(str(self.name)+ '_four_grams.txt','w')
        f.write(str(d))
        f.close

    def read_model(self):
        """reads the dictionaries for the Text model object from a text file
        """
        #read model for words frequencies dictionary
        f = open(str(self.name)+'_words.txt','r')
        d_str = f.read()
        f.close
        self.words = dict(eval(d_str))
        
        #read model for word_lengths dictionary
        f = open(str(self.name) + '_word_lengths.txt','r')
        d_str = f.read()
        f.close
        self.word_lengths = dict(eval(d_str))
        
        #read model for stems dictionary
        f = open(str(self.name)+ '_stems.txt','r')
        d_str = f.read()
        f.close
        self.stems = dict(eval(d_str))
        
        #read model for sentence lengths dictionary
        f = open(str(self.name)+ '_sentence_lengths.txt','r')
        d_str = f.read()
        f.close
        self.sentence_lengths = dict(eval(d_str))

        
        #read model for four adjacent characters dictionary
        f = open(str(self.name)+ '_four_grams.txt','r')
        d_str = f.read()
        f.close
        self.four_grams = dict(eval(d_str))
        
    def similarity_scores(self,other):
        """returns list of similarity scores for
           the dictionary atrributes of the two objects
        """
        word_score = compare_dictionaries(other.words,self.words)
        word_len_score = compare_dictionaries(other.word_lengths,self.word_lengths)
        stem_score = compare_dictionaries(other.stems, self.stems)
        sen_len_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        four_gram_score = compare_dictionaries(other.four_grams,self.four_grams)
        list_scores = [round(word_score,3), round(word_len_score,3),round(stem_score,3),round(sen_len_score,3),round(four_gram_score,3)]
        return list_scores
    
    def classify(self,source1,source2):
        """inputs two sources and compares the similarity scores to the called object
        """
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for', str(source1.name),scores1)
        print('scores for',str(source2.name),scores2)

        relative_score1 = 0
        relative_score2 = 0
        for i in range(len(scores1)):
            if scores1[i] > scores2[i]:
                relative_score1 += 1
            else:
                relative_score2 += 1
        if relative_score1 > relative_score2:
            print(str(self.name) + ' is more likely to have come from '+str(source1.name))
        else:
            print(str(self.name)+ ' is more likely to have come from '+str(source2.name))
        




    
