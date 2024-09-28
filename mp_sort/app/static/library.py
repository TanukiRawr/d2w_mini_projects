from org.transcrypt.stubs.browser import *
import random

def bubble_sort(array: list[int|float]) -> None:
    n = len(array)
    for i in range(0,n-1):
        for j in range (0,n-1):
            firstnum = array[j]
            secondnum = array[j+1]
            if firstnum>secondnum:
                array[j],array[j+1] = array[j+1],array[j]

def list_to_string(list,string:str):
    string = ''
    for i in list:
        string = string + str(i)
        if i == list[9]:
            string = string + "."
        else:
            string = string + ","
    return string

def gen_random_int(number, seed):
	result = None
	ls = []
	random.seed(seed)
	for i in range(number):
		ls.append(i)
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
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	pass
	value = document.getElementsByName("generate")[0].value
      
	array_str = None
	
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

	num = value.split(',')
	bubble_sort(num)
	# Your code should start from here
	# store the final string to the variable array_str
	pass

	array_str = None
	array_str = list_to_string(num,array_str)
	document.getElementById("sorted").innerHTML = array_str


