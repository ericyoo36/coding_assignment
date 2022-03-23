"""
Submission for S&P Global Development Assignment

Problme: Find all palindromes in a string, and print them, 
along with their starting position and length, sorted 
by their length.

Time complexity: O(n), where n = length of input string
Space complexity: O(n), where n = number of palindromes

Date: Mar, 2022
Author: Seongmok (Eric), Yoo 
"""

#find palindromes from input string starting from given start and end index
def find_palindromes(input, start, end):
  while start >= 0 and end < len(input):      #check if start and end index is within a valid range
    if input[start] != input[end]:            #if start and end point character are not equal, its not a palindrome        
      break

    update_dict(input, start, end)            #if palindrome is found, call update_dict to add it to the dictionary
    start -= 1                                #expand start and end by 1 index
    end += 1
  return start, end

#add given palindrome to a dictionary
def update_dict(input, start, end):
  key_string = input[start: end + 1] + "," + str(start)   #construct a key in the form of "palindrome,index"
  palindromes[key_string] = len(input[start: end + 1])    #store length of the palindrome as a value to a key
  return palindromes

#sort the dictionary of "palindrom,index" and length pairs 
def sort_dict(dict):
  sortedDict = sorted(palindromes.items(), reverse=True, key=lambda item: item[1]) #sort the dictionary by its value(length of a palindrome) in decending order
  return sortedDict

#call above functions to generate a output for solution
def solution(input):
  #call find_palindromes for each characters of a given input
  for i in range(0, len(input)):
    find_palindromes(input, i - 1, i + 1)       #set start and end point with difference of two to find palindromes with odd length 
    find_palindromes(input, i, i + 1)           #set start and end point with difeerence of one to find palindromes with even length

  #print solution
  for key, value in sort_dict(palindromes):      #***comment this section for testing***
    print(key + "," + str(value))                #***comment this section for testing***

  return palindromes


palindromes = {}      #declare an empty dictionary

#*******************Enter your desired input String*****************
input_string = "ABCBAHELLOHOWRACECARAREYOUILOVEUEVOLIIAMAIDOINGGOOD"    #***comment this section for testing***
solution(input_string)                                                  #***comment this section for testing***




#********************For Testing Purpose ONLY***********************
#-uncomment each section to test specific unit

#Test for update_dict function
"""
palindromes = {}
result = update_dict("abba" ,1 ,2)
dict = {"bb,1":2}
print(result == dict)
"""

#Test for sort_dict
"""
testcase1 = {"aa,0":2, "bbb.1":3, "cccc,2":4}
testcase2 = {"cccc,2":4, "bbb.1":3, "aa,0":2}
result = sort_dict(testcase1)
print(testcase1 == testcase2)
"""
#Test for find_palindromes (odd length)
"""
result = find_palindromes("abba", 0, 3)
print(result == (-1,4))
"""

#Test for find_palindromes (odd length)
"""
result = find_palindromes("ababa", 0, 4)
print(result == (-1,5))
"""

#Test for solution
"""
palindromes = {}
dict = {"aba,0":3, "cc,3":2}
result = solution("abacc")
print(result == dict)
"""