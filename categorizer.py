#!/usr/bin/env python
# coding: utf-8

# In[86]:


#import dependencies
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


# In[87]:


#read data file
path = "new_dataset.csv"
text_data = pd.read_csv(path, names=['date','text', 'label'], header = 0, encoding = 'utf-8')
#header = 1 tells pandas that file containes 1 header row at index=0


# In[88]:


text_data.shape


# In[89]:


#examine number of communication, code and Web labels
print(text_data["label"].value_counts())
type(text_data["label"])


# In[90]:


#separate text and label into 2 variables
text = text_data.text
label = np.array(text_data["label"], dtype="|S6")  #Multinomial NB only takes integers
#type(label)


# In[91]:


#split training data and test data
text_train, text_test, label_train, label_test = train_test_split(text, label, random_state = 1) 
print("label_test")
print(np.unique(label_test, return_counts = True))

print("\nlabel_train")
print(np.unique(label_train, return_counts = True))


# In[92]:


vect = CountVectorizer(stop_words ="english") #instance of Count vectorizer


# In[93]:


#fit the Count vectorizer aka learn the 'vocabulary' of the text and transform training data into 'document-term matrix (DTM)'
text_train_dtm = vect.fit_transform(text_train.astype(str))


# In[94]:


#examine the document-term matrix (DTM)
text_train_dtm


# In[95]:


#print(text_train_dtm)


# In[96]:


#examine the dense matrix of the DTM and the vocabulary together
pd.DataFrame(text_train_dtm.toarray(), columns=vect.get_feature_names())

#transform testing data into a DTM(using existing vocabulary)
text_test_dtm = vect.transform(text_test.astype(str))
#text_test_dtm.toarray()


# In[97]:


#------import model, train and make prediction with model -------
from sklearn.naive_bayes import MultinomialNB, GaussianNB

#instantiate the Naive Bayes model
nb = MultinomialNB()
#fit_prior = False reduced the accuracy to 71%

gb = GaussianNB()



# '''1. vect.fit(training_data) learns the vocabulary of the training data
# 2. vect.transform(training_data) uses the fitted vocabulary to build a document-term matrix from the training data.
# 3. vect.transform(testing_data) uses the fitted vocabulary to build a document-term matrix from the testing data (and ignores tokens it hasn't seen in the training data)
# '''
# 

# In[98]:


#train the model using the text_train_dtm
nb.fit(text_train_dtm, label_train)
gb.fit(text_train_dtm.toarray(), label_train) #only accepts dense matrix


# In[99]:


#make class prediction for text_test_dtm
nb_predictions = nb.predict(text_test_dtm)
gb_predictions = gb.predict(text_test_dtm.toarray()) #only accepts dense matrix


# # -----------------calculate accuracy-------------------------
# 

# In[100]:


#import accuracy score module
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# In[101]:


#calculate accuracy of the prediction
nb_accuracy = accuracy_score(label_test, nb_predictions)
gb_accuracy = accuracy_score(label_test, gb_predictions)

#examine the accuracy
print(f"MultinomialNB accuracy = {round(nb_accuracy,3) * 100}%")
print(f"GaussianNB accuracy = {round(gb_accuracy,3) * 100}%")


# In[108]:


#----------------build confusion matrix----------------------

conf_mat = confusion_matrix(label_test, nb_predictions, labels = np.unique(label_test))
#print("chat cloud code mail office other script web']")

label_names = []
for x in np.unique(label_test):
    label_names.append((x.decode()).upper())

    
print(pd.DataFrame(conf_mat, index = label_names, columns = label_names))


# In[103]:


#----------------build confusion matrix----------------------

conf_mat = confusion_matrix(label_test, gb_predictions)
print("GaussianNB \nCode Comm Web")
print(conf_mat)


# In[104]:


# print the classification report
print("MultinomialNB Classification Report \n")
print(classification_report(label_test, nb_predictions))


# In[105]:


# print the classification report
print("GaussianNB Classification Report \n")
print(classification_report(label_test, gb_predictions))


# In[106]:


d = {"text":text_test, "actual_label":label_test, "predicted_labels": nb_predictions}
df = pd.DataFrame(d)
df.to_excel("Prediction_Results2.xlsx")


# In[110]:


#----Save the trained model to a pickle file ---------

from sklearn.externals import joblib 
  
# Save the model as a pickle in a file 
joblib.dump(nb, 'categorizer.pkl') 
joblib.dump(vect, 'transformer.pkl')
  
# Load the model from the file 
#knn_from_joblib = joblib.load('filename.pkl')  
  
# Use the loaded model to make predictions 
#knn_from_joblib.predict(X_test)


# In[ ]:




