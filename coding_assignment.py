"""

Problme: Find all palindromes in a string, and print them, 
along with their starting position and length, sorted 
by their length.

Time complexity: O(n), where n = length of input string
Space complexity: O(n), where n = number of palindromes

Date: Mar, 2022
Author: Seongmok (Eric), Yoo 
"""


#find palindromes from input string starting from given start and end index
def find_palindromes(dict, input, start, end):

  while start >= 0 and end < len(input):      
    if input[start] != input[end]:                #if it is not a palindrome, break out of the loop       
      break

    update_dict(dict, input, start, end)          #if it is a palindrome, add it to the dictionary
    start -= 1                                    #expand start and end by 1 index
    end += 1

  return start, end


#add given palindrome to a dictionary
def update_dict(dict, input, start, end):

  key_string = input[start: end + 1] + "," + str(start)   #construct a key in the form of "palindrome,index"
  dict[key_string] = len(input[start: end + 1])           #store length of the palindrome as a value to a key

  return dict


#sort the dictionary
def sort_dict(dict):

  sortedDict = sorted(dict.items(), reverse=True, key=lambda item: item[1]) #sort the dictionary by its value in decending order

  return sortedDict


#call above functions to generate a output for solution
def solution(input):
  palindromes = {} 

  for i in range(0, len(input)):
    find_palindromes(palindromes, input, i - 1, i + 1)       #find palindromes with odd length 
    find_palindromes(palindromes, input, i, i + 1)           #find palindromes with even length

  #print solution
  for key, value in sort_dict(palindromes):      #***comment this section for testing***
    print(key + "," + str(value))                #***comment this section for testing***

  return palindromes


palindromes = {} 
#*******************Enter your desired input String as input_string*****************
input_string = "ABCBAHELLOHOWRACECARAREYOUILOVEUEVOLIIAMAIDOINGGOOD"          #***comment this section for testing***
solution(input_string)                                           #***comment this section for testing***
