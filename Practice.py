




 


#1. Reverse a String in Python
#def firstReverse(str):
#	return str[::-1]

#print firstReverse("hello world")


#1b. Simple Reverse
#"hello world" [::-1]



#Double a string
#def doubling(li):
#	newList = []
#	for i in range(0, len(li)):
#		result = li[i] * li[i]
#		newList.append(result)
#	return newList

#print doubling([1, 2, 3, 4])
		

#2 Letter Changes in Python
#def LetterChanges(str):
#	newString = ""
	
#	for char in str:
#		if char.isalpha():
#			if char.lower() == "z":
#				char = "a"
#			else:
#				char = chr(ord(char) + 1)
#		if char in "aeiou":
#			char = char.upper()
#		newString = newString + char
		
#	return newString
# print LetterChanges("It is a new world out here!")


#3 Capitalizing the First Letter of each word in Python
#def LetterCapitalize(str):
#	return str.title()

#print LetterCapitalize("hello the brave new world")


#4 Checking Simple Symbols in strings in Python

#def SimpleSymbols(str): 
  
  # pad the strings so that if a character exists at the beginning
  # of the string for example, we don't get on out-of-bounds error by
  # trying to get the character before it
#  str = '=' + str + '='

  # loop through the entire string
#  for i in range(0, len(str)):
    
    # check to see if current character is an alphabetic character  
  #  if str[i].isalpha():

      # check to see if a + symbol is to the left and right
      # if not, then we know this string is not valid
 #     if str[i-1] != '+' or str[i+1] != '+':
 #       return 'false'

 # return 'true'

# print SimpleSymbols("+d+=3=+s+")    


#5 Return Factorials in Python 

#5a, simple version

#num = 8
#print num*7*6*5*4*3*2*1 

#5b
#num = 8
#def firstFactorial(num):
#	return num*7*6*5*4*3*2*1
#print firstFactorial(num)




#5c
#def FirstFactorial(num): 

 # factorial = 1
  
#  for i in range(1, num+1):
    # multiply each number between 1 and num  
    # factorial = 1 * 1 = 1
    # factorial = 1 * 2 = 2
    # factorial = 2 * 3 = 6
    # factorial = 6 * 4 = 24
    # ...
  #  factorial = factorial * i

#  return factorial

# print FirstFactorial(4)       



# 6. Simple Adding in Python
#def simpleAdding(num):
#	return sum(range(1, num + 1))
 #print simpleAdding(4)
	
	
# 7. Check Numbers in Python
# def CheckNums(num1, num2):
#	if num2 > num1:
#		return "true"
#	elif num2 < num1:
#		return "false"
#	return "-1"
# print CheckNums(5, 5)



# 8. Converting Time in Python

# import math

# def TimeConvert(num): 

  # to get the hours, we divide num by 60 and round it down
  # e.g. 61 / 60 = 1 hour
  # e.g. 43 / 60 = 0 hours
 # hours = int(math.floor(num / 60))

  # to get the minutes, now we use the remainder that we discarded above
  # the modulo operation is represented by the % symbol
  # e.g. 61 % 60 = 1 minute
  # e.g. 43 % 60 = 43 minutes
 # minutes = num % 60

  # combine the hours and minutes
 # return str(hours) + ':' + str(minutes);
    

# 9. Finding Lowest Word in Python
# def LongestWord(sen): 

  # first we remove non alphanumeric characters from the string
  # using the translate function which deletes the specified characters
 # sen = sen.translate(None, "~!@#$%^&*()-_+={}[]:;'<>?/,.|`")

  # now we separate the string into a list of words
 # arr = sen.split(" ")

  # the list max function will return the element in arr
  # with the longest length because we specify key=len
 # return max(arr, key=len)
    
# print LongestWord("the $$$longest# word is coderbyte")  



# 10. Sort string in alphabetical order in Python

	
#def AlphabetSoup(str):
#	chars = list(str)
#	sortedChars = sorted(chars)
#	return "".join(sortedChars)
#print AlphabetSoup("hello world")
 








