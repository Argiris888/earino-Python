from scipy.spatial import distance_matrix

import csv

import numpy as np

from Plotting import MyPlot

from CSVreader import extractColumnsAsTuplesFromfile

from KNNeighbours import FindKNearestNeighboursInThePath

from weightedAverageDistances import ListOfWeightedDistances

from NormalizingFunction import NormalizingListOfWeightedDistances



#creating array from my given data using this function
coordinates_List_Of_Tuples=extractColumnsAsTuplesFromfile(filename='GreekCities.txt')

#creating a matrix filled with all the possible distances between my given points of visit       
my_distance_matrix=np.array(distance_matrix(coordinates_List_Of_Tuples,coordinates_List_Of_Tuples))

#number of visits in order to visit each point and return to start point
numberOfVisits=len(coordinates_List_Of_Tuples)

#the number of nearest neighbours that we are going to use in order to randomly choose one of them based on each neighbour's probability
numberOfNearestNeighbours=5

#the number of repeats that algorithm is going to go through, for finding the path with minimum distance
numberOfAlgorithmReps=500

##the starting and ending point of my path
#myNextPointOfVisit=0

##the list of points of my path for every repetition
#myPath=[0]

##the total distances for the path of each repetition
#totalDistanceOfPath=0

#the number of power that we are going to use for the creation of weigthed distances of my k nearest neighbours
powerUsedToWeightedDistance=20

#a list filled with the path(list of points) from each repetinion. Its a list of lists
listOfRepPaths=[]

#a list filled with the distances from each path for every repetition. Its a list of float numbers
listOfRepDistances=[]


#loops based on the number of loops that we are going to choose in order to select best path
for reps in range(numberOfAlgorithmReps):

       #the starting and ending point of my path
       myNextPointOfVisit=0

       #the list of points of my path for every repetition
       myPath=[0]

       #the total distances for the path of each repetition
       totalDistanceOfPath=0
       # finding a path for each repetition, we use -1 because we dont include ending point
       # in each repetiion of this process we gonna find my next point of visit and its k nearest neighbours  until there is no more points for visit, except the starting point
       for i in range(numberOfVisits-1):

           #to make sure that we dont gonna have empty list of nearest neighbours
           if numberOfVisits!=len(myPath):
             
                    #using the function that returnes a tuple of 2 lists:t he list of k nearest points from my present point, and the list of the distances between my present point and k nearest neighbours
                    listOfNearestNeighbours,listOfDistances=FindKNearestNeighboursInThePath(my_distance_matrix,numberOfNearestNeighbours,myNextPointOfVisit,myPath)
                    
                    #using the function for returning a list of the weighted distances for my k nearest neighbours for my present point
                    weightedListOfNN=ListOfWeightedDistances(listOfDistances,powerUsedToWeightedDistance)
                    
                    #normalizing the list of the weighted distances between my present point and its k nearest neighbours
                    normalizedList=NormalizingListOfWeightedDistances(weightedListOfNN)
                    
                    #randomly choosing my next point of visit from my list of my present's point k nearest neighbours, based on the probability of each neighbour
                    myNextPointOfVisit=np.random.choice(listOfNearestNeighbours, p=normalizedList) 
                    
                    NextPointOfVisitDistance=listOfDistances[list(listOfNearestNeighbours).index(myNextPointOfVisit)]
                    
                    #adding my next point of visit to my path list, for this repetition
                    myPath.append(myNextPointOfVisit)
                    
                    #calculating the total distance of my path for this repetition
                    totalDistanceOfPath+=NextPointOfVisitDistance
                    
       
       #from each repetition we have a path, so we add this path in a list which is finally filled with all the paths from my repititions
       listOfRepPaths.append(myPath)

       #a list filled with the distances of each path
       listOfRepDistances.append(totalDistanceOfPath)
       
       
           
           
#finding the minimum distance within  my  list  of paths distances created by the upper set of repetitions
minimumDistance=min(listOfRepDistances)

#finding the path with the minimum distance created by the upper set of repetitions
indexOfPathWithMinimumDistance=list(listOfRepDistances).index(minimumDistance)

pathWithMinimumDistance=listOfRepPaths[indexOfPathWithMinimumDistance]

#adding the final point of the final path from the upper set of repititions, that is the starting point
minimumDistance+=my_distance_matrix[myNextPointOfVisit][myPath[0]]

#adding in total distance of the final path the distance between the last visited point and the starting point
pathWithMinimumDistance.append(myPath[0])

print(pathWithMinimumDistance)

print(minimumDistance)


#plotting the final path from this set of repetitions
coordinates_List_Of_Tuples = [coordinates_List_Of_Tuples[i] for i in pathWithMinimumDistance]

MyPlot(coordinates_List_Of_Tuples)



