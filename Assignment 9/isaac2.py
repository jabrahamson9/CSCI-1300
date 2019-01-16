

def main():
	listOfNames = ["Amira", "Stacy", "Heather", "Michael", "Abas", "Johann"]
	index = 0
	for name in listOfNames:
		if index % 2 == 1:
			listOfNames.remove(name)
		index += 1
	print(listOfNames)


if __name__=="__main__":
	main() 