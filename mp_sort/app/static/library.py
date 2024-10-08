from org.transcrypt.stubs.browser import *
import random

def bubble_sort(array: list[int|float]) -> None:
    # bubble sort
    n = len(array)

	# checking if the left number is larger than the right number, and if so, swap
    # Will check for all the outer and inner iterations
    # Ensures the numbers are float
    for i in range(0,n-1):
        for j in range (0,n-1):
            firstnum = float(array[j])
            secondnum = float(array[j+1])
            if firstnum>secondnum:
                array[j],array[j+1] = array[j+1],array[j]
                
#Changing a list of int/float to string
def list_to_string(ls,string:str):
    string = ''
    num = len(ls)
    # for every element in the list, add to string with a comma and ends the string with a .
    for i in range(0,num):
        string = string + str(ls[i])
        if i == (num-1):
            string = string + "."
        else:
            string = string + ","
    return string

#generating a random list of integer with a given number of elements inside and seed
def gen_random_int(number, seed):
	result = None
	ls = []
	random.seed(seed)
    # the range of random int is from 0 - 100 to make the sorting more apparent
	for i in range(number):
		ls.append(random.randint(0,100))
            
	random.shuffle(ls)
	result = ls
	return result
	pass

def generate():
	number = 10
	seed = 200
	# call gen_random_int() with the given number and seed
	# store it to the variable array
	pass

	array = None
	array = gen_random_int(number,seed)
	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.
	pass

	array_str = None
	array_str = list_to_string(array,array_str)
	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str


def sortnumber1():
	'''	This function is used in Exercise 1.
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	generated_numbers = document.getElementById("generate").innerHTML
    
	#removes the .
	generated_numbers = generated_numbers[:-1]
      
	#split the string into a list of char
	array_of_char = (generated_numbers.split(','))
    
	#bubble sort the list of char (the bubble sort functions turns the char into float)
	bubble_sort(array_of_char) 
	array_str = None
      
	#changes the list of float into a string to show on the website
	array_str = list_to_string(array_of_char,array_str)
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	#splits the string and sort it into a list of float
	num = (value.split(','))
	bubble_sort(num)
	# Your code should start from here
	# store the final string to the variable array_str
	pass

	array_str = None
    #Change the list to string to show on the website
	array_str = list_to_string(num,array_str)
	document.getElementById("sorted").innerHTML = array_str