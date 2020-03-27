import numpy as np
minGrade=0
maxGrade=100

minNumberOfEachClass=0
maxNumberOfEachClass=60

# Size of Class A and random Grades of each individual
classA_numberOfStudents=np.random.randint( minNumberOfEachClass, maxNumberOfEachClass)
classA_grades= np.random.randint( minGrade, maxGrade, classA_numberOfStudents)

# Size of Class A and random Grades of each individual
classB_numberOfStudents=np.random.randint( minNumberOfEachClass, maxNumberOfEachClass)
classB_grades= np.random.randint( minGrade, maxGrade, classB_numberOfStudents)

# Unique Grades for Both Classes
uniqueGradesOfBothClasses=set(classA_grades)|set(classB_grades)

# Finding and Counting the Similar Grades Between Class A and Class B
countOfSimilarGrades=0
list_of_similarGrades=[]
for grade in set(classA_grades):
    if grade in set(classB_grades):
        countOfSimilarGrades+=1
        list_of_similarGrades.append(grade)

print(f'The list of similar grades within Class A and Class B is {list_of_similarGrades} \nTotal number of similar Grades: {countOfSimilarGrades}')

