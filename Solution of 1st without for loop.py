import numpy

import array
    
# Username we are searching for
searchForClientSurname='karag'

# Array of tuples filled with clients elements
bankClients= numpy. array((('ar','var',234),('nik','ver',134),('kwst','lonr',654),('man','karag',598)))   

# List filled with the surnames of the clients
listOfSurnames=bankClients[:,1]

# The Bank account which is owned by the client we are searching for
BankAccount_Number=int(bankClients[listOfSurnames==searchForClientSurname,2])

print(f'The Bank Account of mrs/mr "{searchForClientSurname.upper()}" is  {BankAccount_Number}')



