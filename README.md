# Markov Model for Text Analysis
A simple markov model that inputs two bodies of text to create a working model for text comparison. The model will analyze the semantics of the text based on five categories, the stem of the words, the sentence lengths, word frequencies, word lengths, and adjacent characters.  

# Getting Started
1. Clone Repository
2. Take the two bodies of text you want to create the model from and place them in respective text files, and take one additional sample text

## How to Test
1. Create model objects for each text you use to compare, and use the add_file() method to add the two text files you want to compare
2. Add sample text you want to compare to the two base texts 
3. Use the classify() method to compare your model class with the sample text against the two model classes made up of the bigger pieces of text
4. The method will print out a variety of scores based on the categories used for comparison, and will tell you what body of text your sample is most similar to 
