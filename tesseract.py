#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import tesseract for OCR and PILLOW to parse screenshots
from pytesseract import image_to_string
from PIL import Image
import pytesseract



# In[2]:


from os import listdir

#path to the main directory of screenshots
mypath = "/screenshots/"


# In[3]:


def get_employee():
    employees=[] #list of directory names
    for name in listdir(mypath):
        employees.append(mypath+"/"+name)
        
    date_folders(employees)
   


# In[4]:


def date_folders(employees):
    #get date folder names inside every employee's folder
    dates = []
    for e in employees:
        for date in listdir(e):
            dates.append(e+"/"+date)
            
    screenshots_to_text(dates)


# In[7]:


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
def screenshots_to_text(dates):
    size = 7016, 4961
    screenshots = []
    for d in dates:
        for screenshot in listdir(d):
            screenshots.append(d+"/"+screenshot)
            #implement pytesseract's OCR here
        for image in screenshots:
            im = Image.open(image)
            im = im.resize(size, Image.ANTIALIAS)
            f= open(image+".txt","w+") 
        #add the OCR results to the screenshot.txt
            f.write(image_to_string(im, lang="eng+fra")) 
        #close the screenshot file
            f.close()
get_employee()


# In[ ]:





# In[ ]:




