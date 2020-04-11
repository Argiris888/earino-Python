# 1th Function

def covid19_Function_import_Country():
     nameOfCountry=input('Give me the name of the country: ')
     casesOrDeaths=input('What data shall I report on? Type \'1\' for Cases and \'2\' for Deaths: ')
     if casesOrDeaths=='1':
         columnOfInterest=4
     elif casesOrDeaths=='2':
         columnOfInterest=5
     return[nameOfCountry,columnOfInterest]
        



# 2th Function 

def  covid19_Function_CsvFile(Imported_csv_file,Country_Name):
   import csv
   import numpy as np
   with open(Imported_csv_file,newline='') as csvfile:
       spamreader=csv.reader(csvfile,delimiter=',')
       filtered_rows =[]
       count=0
       Infected_Countries=set()
       for row in spamreader:

          Infected_Countries.add(row[6])
          if row[6]==Country_Name:
              count+=1
              filtered_rows.append(row)
              
          
       if count==0:
            print(' , '.join(Infected_Countries))
       else:
         
          return [np.array(filtered_rows)]


       
   
          
     
  







