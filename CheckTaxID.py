def CheckIfValid(TaxId):

    myListOfTaxIDDigits=[]

    # making a list of number out of a given string with numbers
    for number in str(TaxId):
         
        myListOfTaxIDDigits.append(int(number))

    # in order to use the reversed list
    reversedList=myListOfTaxIDDigits[::-1]


    i=1
    cumSum=0

    # calculating the cumSum of the digits
    for digit in reversedList[1:8]:

        
        cumSum += (2**i) * digit

        i+=1

    # checking the validation of TAXID     
    if (cumSum%11)==myListOfTaxIDDigits[-1] :

           print(f'The Tax ID {TaxId} is valid')

    else:
         
           print(f'The Tax ID {TaxId} is not valid') 
   




CheckIfValid(284596895)