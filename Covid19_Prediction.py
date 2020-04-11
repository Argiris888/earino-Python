import numpy as np
from matplotlib import pyplot as plt 
#from covid19_Functions import covid19_Function_CsvFile, covid19_Function_import_Country



# 1st Function -Input of Country's Name and option between cases and deaths of Covid19

def covid19_Function_import_Country():
     nameOfCountry=input('Give me the name of the country: ')
     casesOrDeaths=input('What data shall I report on? Type \'1\' for Cases and \'2\' for Deaths: ')
     if casesOrDeaths=='1':
         columnOfInterest=4
     elif casesOrDeaths=='2':
         columnOfInterest=5
     return[nameOfCountry,columnOfInterest]
        





# 2th Function - Function for creating array filled with  chosen Country's Covid19 data, from CSV file 

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







# Main Script



# Name Of Country under investigation
CountrysNameForResearch, Case_Or_Death_Column=covid19_Function_import_Country()

# Covid19 Data of Country 
Array_Of_Infected_Country=covid19_Function_CsvFile('myFile.csv',CountrysNameForResearch)[0]


# Column Of chosen Incedend: Cases or Deaths
MyColumnOfChoice=[]

for day,element in enumerate(Array_Of_Infected_Country):
     MyColumnOfChoice.append(int(element[5]))
     
MyReversedColumnOfChoice=MyColumnOfChoice[::-1]

# Finding the first day of  Covid19 incident in the chosen country
my_index=MyReversedColumnOfChoice.index(not 0)


# Final Column of Incidends
MyFinalList=np.cumsum(MyReversedColumnOfChoice[my_index:])


# Column of Days Since First Incident
DaysColumn=list(range(1,len(MyNumericalColumn)-my_index+1))



# Concatenating both columns to one Array
Covid_Array=np.array([DaysColumn,MyFinalList]).transpose()


# Calculating Total Days since First Covid19 Incidend
DaysSinceFirstIncident=len(DaysColumn)


# Calculating the Covid19 Coefficients Of choosen Country Polynomial
x=np.array(DaysColumn)
y=np.array(MyFinalList)
CoefficientsOfPolynomial=np.polyfit(x,y,3)



# Predicting and Visualizing Country's Data for next 3 days

DaysOfPrediction=3
TotalPointsForLinspace=100

X_Outlines=np.linspace(1,DaysSinceFirstIncident+DaysOfPrediction,100)

Y_Values=np.polyval(CoefficientsOfPolynomial, X_Outlines)


plt.title("Projection line") 
plt.xlabel("Days since 1st incident") 
plt.ylabel("Incidends") 
plt.plot(X_Outlines,Y_Values) 
plt.show()

