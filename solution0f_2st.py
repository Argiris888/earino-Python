import numpy as np
minGrade=0
maxGrade=100

minNumberOfEachClass=0
maxNumberOfEachClass=60

# Size of Class A and random Grades of each individual
classA_numberOfStudents=np.random.randint( minNumberOfEachClass, maxNumberOfEachClass)
classA_grades= np.random.randint( minGrade, maxGrade,classA_numberOfStudents)

# Size of Class A and random Grades of each individual
classB_numberOfStudents=np.random.randint( minNumberOfEachClass, maxNumberOfEachClass)
classB_grades= np.random.randint( minGrade, maxGrade, classB_numberOfStudents)

# Unique Grades for Both Classes
uniqueGradesOfBothClasses=set(classA_grades)|set(classB_grades)

# Finding and Counting the Common Grades Between Class A and Class B
countOfCommonGrades=0
list_of_CommonGrades=[]
for grade in set(classA_grades):
    if grade in set(classB_grades):
        countOfCommonGrades+=1
        list_of_CommonGrades.append(grade)

print(f'The list of Common grades within Class A and Class B is {list_of_CommonGrades} \nTotal number of Common Grades: {countOfCommonGrades}')

