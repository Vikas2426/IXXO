#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import tesseract for OCR and PILLOW to parse screenshots
from pytesseract import image_to_string
from PIL import Image
import pytesseract
from os import listdir
from os import mkdir


# In[2]:


#path to the main directory of screenshots
mypath = "C:/Users/Vikas/Downloads/screenshots/"


# In[3]:


#create folders for output files
def make_dir(path):
    mkdir(path)


# In[4]:


def get_employee():
    employees_input=[] #list of input employee folders
    employees_output = [] #list of output employee folders
    
    for name in listdir(mypath):
        output_path = "C:/Users/Vikas/Downloads/Output/"+name
        employees_output.append(output_path)
        make_dir(output_path)
        employees_input.append(mypath+"/"+name)
        
    date_folders(employees_input, employees_output)
 


# In[5]:


def date_folders(employees_input, employees_output):
        
    dates_input = [] #list of input employee->date folder
    dates_output = [] #list of output employee->date folder
    
    #get date folder names inside every employee's folder
    for a, b in zip(employees_input, employees_output):
        for date in listdir(a):
            output_path = b+"/"+date
            dates_output.append(output_path)
            make_dir(output_path)
            dates_input.append(a+"/"+date)
            
    screenshots_to_text(dates_input, dates_output)


# In[6]:


#Add tesseract to path
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

def screenshots_to_text(dates_input, date_output):
    size = 7016, 4961 #size for 300 dpi image
    
    screenshots = [] #list of input employee->date->screenshots
    screenshot_output_names = [] #list of input employee->date->screenshot names
    
    for a, b  in zip(dates_input, date_output):
        for screenshot in listdir(a):
            screenshot_output_names.append(b+"/"+screenshot)
            screenshots.append(a+"/"+screenshot)
            
            #implement pytesseract's OCR here
        for image, image_name in zip(screenshots, screenshot_output_names):
            im = Image.open(image)
            im = im.resize(size, Image.ANTIALIAS) #resize image to 300dpi for better results
            
        #open a txt file for OCR results    
            f= open(image_name+".txt","w+")
            
        #add the OCR results to the screenshot.txt
            f.write(image_to_string(im, lang="eng+fra"))
            
        #close the output file
            f.close()


# In[ ]:


get_employee()
