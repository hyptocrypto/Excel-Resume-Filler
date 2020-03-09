'''This program extracts name, job, email and phone number info from PDF files
(spesificaly Medical Personnel Resumes from indeed) and the writes that info into an csv file. '''



from pdfminer import high_level
import re
import os 
import pandas as pd 

# Directory where Resume PDF's are stored
localdir = '/Users/julianbaumgartner/Desktop/Python/Excel_Resume_Fill/Resumes'

# Empty variables to append as we parse the PDF's
name = []
job = []
emails = []
phone_number = []

# Iterate over each file in the localdir. If it is a PDF file, extract job, email and phone number
# and append them in the coresponding variable above.  
for filename in os.listdir(localdir):
    if filename.endswith('.pdf'):
        text = high_level.extract_text(localdir + '/' + filename)

    try:
        job.append(re.search(r'Home Health Aide|home health aide|Home health aide|caregiver|homemaker|Caregiver|Homemaker|CNA|HHA|LPN|RN|cna|hha|lpn', text).group())
    except AttributeError:
        job.append('No Job Found')
    
    name.append(filename[:-4])
    
    emails.append(re.search("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", text).group())

    phone_number.append(re.search(('\(?\d{3}\)?[-\.]? *\d{3}[-\.]? *[-\.]?\d{4}'),text).group())

    

# Construct the data to format into Data Frame    
raw_data = {'Name': name,'Job': job, 'Email': emails, 'Phone_Number': phone_number}

# Create Data Frame     
resumeDF = pd.DataFrame(raw_data, columns = ['Name','Job','Email','Phone_Number'])
        
# Sort Data Frame by job
sorted_resumeDF = resumeDF.sort_values(by = ['Job'])

# Write the Data Frame to a CSV file
sorted_resumeDF.to_csv('/Users/julianbaumgartner/Desktop/Python/Excel_Resume_Fill/Resumes.csv')