
### 1h Askhsh

#my_given_sentence='Kai ela kai pes mou kainouria pragmata kai ti kaneis '
##  #len_of_sentence=len(my_given_sentence) e
##  #print(f'to mhkos ths sumvoloseiras einai {len(my_given_sentence)}') e
#list_of_words=my_given_sentence.strip().split(' ')
#print(f'o arithmos twn leksewn einai {len(list_of_words)}')



### 2h Askhsh

##count_of_whitespaces=my_given_sentence.count(' ')
##sum_of_chars=len(my_given_sentence)-count_of_whitespaces
##print(f'o aritmos twn xarakrhwn dixws ta kena einai {sum_of_chars}')

### 3h Askhsh
#given_word='kai'
#number_of_word_in_block=my_given_sentence.count('Kai ') + my_given_sentence.count(' kai ')
#print('o arithmos twn leksewn \'{}\' sthn protash: \'{}\' einai {}'.format(given_word,my_given_sentence,number_of_word_in_block))

### 4h Askhsh


startingIndex = 2

endingIndex = 6

startingZeroBasedIndex = startingIndex - 1

objToReplaceWith = 55

myList=[4,6,2,8,9,1,5,9,5,2]

myList[startingZeroBasedIndex:endingIndex] = [objToReplaceWith] * (endingIndex - startingZeroBasedIndex)

print(myList)                









