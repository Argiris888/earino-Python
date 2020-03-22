import array as ar
import numpy as np
lowerRange=0
upperRange=101
size=100
my_array_1=np.random.randint(lowerRange,upperRange,size)
#print(my_array_1)

my_array_2=np.random.randint(lowerRange,upperRange,size)

addedArrays=my_array_1 + my_array_2
print(addedArrays)

numberToLookFor=87
myPythonArray=ar.array('i',addedArrays)
numberOfOccurances=myPythonArray.count(numberToLookFor)
print(f'to {numberToLookFor} emfanizetai {numberOfOccurances} fores ston pinaka')

# posa stoixeia einai megalutera apo 87; ektupwse ta

myLogicalArrow=addedArrays>numberToLookFor    #mono se numpy pinaka ginetai logikh sugkrish 
myPythonLogArray=ar.array('i',myLogicalArrow)

print(myPythonLogArray.count(1))   #gia a ksanaxrhsimopoihsw th count

myNewArray=addedArrays[myLogicalArrow]

print(f'\n{myNewArray}')   #pinakas me stoixeia megalutera tou 87



