def writeto(filename, listOfStuff):
	file = open(filename, "w")
	for item in listOfStuff:
		file.write(str(item) + "\n")


def main():
	
	writeto("writetofile.txt", ["bannana", "pear", "apple"])


if __name__=="__main__":
	main() 