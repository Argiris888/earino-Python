import numpy as np
minGrade=0
maxGrade=100

minNumberOfEachClass=0
maxNumberOfEachClass=60

classA_numberOfStudents=np.random.randint( minNumberOfEachClass, maxNumberOfEachClass)
classA_grades= np.random.randint( minGrade, maxGrade, classA_numberOfStudents)

classB_numberOfStudents=np.random.randint( minNumberOfEachClass, maxNumberOfEachClass)
classB_grades= np.random.randint( minGrade, maxGrade, classB_numberOfStudents)

uniqueGradesOfBothClasses=set(classA_grades)|set(classB_grades)

countOfSimilarGrades=0
list_of_similarGrades=[]
for grade in set(classA_grades):
    if grade in set(classB_grades):
        countOfSimilarGrades+=1
        list_of_similarGrades.append(grade)

print(list_of_similarGrades,countOfSimilarGrades)

