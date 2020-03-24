import numpy

import array
# column where Bank Number is located
columnOfBankNumber=2

#column where Surname is located
columnOfSurname=1    

searchForSurname='karag'


#customer's database
bankClients= numpy. array((('ar','var',234),('nik','ver',134),('kwst','lonr',654),('man','karag',598)))   

#List of Customer's Usernames
listOfSurnames=[ customer[ columnOfSurname] for customer in bankClients]

# Index of Customer in database
searchForIndex= listOfSurnames.index( searchForSurname) 

# the bank number of the customer whom we are searching for
banknumberOfCustomer= bankClients[ searchForIndex][ columnOfBankNumber] 

print(f'The Bank Account of mrs/mr "{searchForSurname.upper()}" is  {banknumberOfCustomer}')
