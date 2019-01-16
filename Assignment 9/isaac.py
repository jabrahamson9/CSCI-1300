def compareTwoNumbers(num1, num2):
	if type(num1) != int or type(num2) != int:
		if type(num1) != float or type(num2) != float:
			print("Invalid arguments supplied")
	else:
		if(num1==num2):
			print("Numbers are equal")
		elif (num1>num2):
			print("The larger number is {}".format(num1))
		else:
			print("The larger number is {}".format(num2))

def printSomeNumbers(myNum, iterationCount, doSummation):
	if doSummation == False:
		for i in range(iterationCount):
			print(myNum)
	elif doSummation == True:
		New = myNum
		for i in range(iterationCount):
			print(New)
			New = New + myNum

def mashItUp(listOfStrings, stepSize):
	str=""
	if type(stepSize) != int or stepSize<1:
		print("Invalid step size")	
		return None
	else:
		for item in listOfStrings:
			for j in range(0, len(item), stepSize):
				str+=item[j]
		return str


def processList(listOfThings, action, thing):
	if action=="delete":
		value = False
		for item in listOfThings:
			if item == thing:
				listOfThings.remove(item)
				value = True
		if value == False:
			print("{} not found in list".format(thing))
		else:
			print(listOfThings)
	elif action == "deleteall":
		if thing in listOfThings:
			listOfThings = list(filter(lambda x:x!=thing, listOfThings))
			print(listOfThings)
		else:
			print("thing not found in list")
	elif action == "append":
		listOfThings.append(thing)
		print(listOfThings)
	elif action == "insert":
		listOfThings = [thing] + listOfThings
		print(listOfThings)







def main():

	lister=["hello", "christmas", "yesterday", "small", "small", "hello"]
	processList(lister, "delete", "sfdasfd")

if __name__=="__main__":
	main() 