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

# Unique Grades in each Class
UniqueGradesOfClassA=set(classA_grades)
UniqueGradesOfClassB=set(classB_grades)

# Intersection set filled with Common grades between ClassA and ClassB
SetOfCommonGrades=UniqueGradesOfClassA.intersection(UniqueGradesOfClassB)

# Number of Common Grades between ClassA and ClassB
numberOfCommonGrades=len(SetOfCommonGrades)

# Check and print if there are common grades between ClassA and ClassB
if numberOfCommonGrades!=0:
    print(f'The Common grades between Class A and Class B are {SetOfCommonGrades} \nTotal number of Common Grades: {numberOfCommonGrades}')
else:
    print(f'There is no common Grade between Class A and Class B')



