import nltk 
nltk.download("stopwords") 
nltk.download("omw-1.4") 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer 
from nltk.stem import WordNetLemmatizer 
nltk.download("punkt") 
nltk.download("stopwords") 
nltk.download("wordnet") 
text = input("Enter the text:") 

tokens = word_tokenize(text) 
stop_words = set(stopwords.words("english")) 
filtered_tokens = [word for word in tokens if word.lower() not in stop_words] 
stemmer = PorterStemmer() 
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens] 
lemmatizer = WordNetLemmatizer() 
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens] 



print("\nTokenized:", tokens) 
print("Stop Word Removal:", filtered_tokens) 
print("Stemming:", stemmed_tokens) 
print("Lemmatization:", lemmatized_tokens)
