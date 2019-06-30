Internship Project Repositories
This repository contains my project which I did as a data science internship.

1. Using Tesseract-OCR, extracted text from employees' screenshots.
2. Prepared a dataset of the Ocred text.
3. Trained a Logistic Regression Model to classify the texts into Code, Web, Email, Chat, Office etc categories.
4. Cleaned those OCRed and classifed text for better readability.

Contents of this repository:
1. categorizer.pkl - pickel file of the trained logistic regression model.
2. categorizer.py - python file of the code.
3. correct_chat, correct_code, correct_mail, correct_office, correct_web - modules to       clean the OCRed and classified text according to its classification.
4. tesseract + categorizer.ipynb - jupyter notebook of the OCR and classifier code.
5. transformer.pkl - pickel file of the trained count vectorizer, which was used to transform the OCRed text into vector for machine learning model training.


