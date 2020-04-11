def createDictionary(startPoint,endPoint):
   myDictionary = {}
   startPoint=1
   endPoint=21
   for a, b in enumerate(list(range(startPoint,endPoint))):
                myDictionary[str(a + 1)] = b ** 2
   return myDictionary
   print(myDictionary.values())


