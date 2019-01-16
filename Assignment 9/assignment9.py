#Jon Abrahamson
#CSCI 1300-108
#Assignment 9
#DUE: 3 December 2017

"""This function takes a list of rates as well as an integer population as parameters
It then uses these rates by taking them from the index of the list and adds or subtracts
these calues from the current population based on if they are births, immigration, or deats
The function then returns the calculated projected population after one year
"""
def compute_census(list_of_rates, current_population):
	projected= int(current_population+(31536000/list_of_rates[0]) + (31536000/list_of_rates[2]) - (31536000/list_of_rates[1]))
	return projected

"""This function takes in no parameters. It then asks for a user input in which the user will insert a number
of seconds. The fucntion then turns this input string into a integer value so it can be worked with in the math
the function then converts the seconds inputted into the number of days, hours, minutes, and seconds
and then finally prints all of these values into a string.
"""
def convert_seconds():
	user_input=input()#inout without any string prompt
	user_input=int(user_input)
	days=int(user_input/86400)
	secondsB=int(user_input%86400)#these modules find left over seconds
	hours=int(secondsB/3600)
	secondsC=int(secondsB%3600)
	minutes=int(secondsC/60)
	secondsD=int(secondsC%60)#must use int to make it from being a float decimal
	print("{} corresponds to: {} days, {} hours, {} minutes, {} seconds.".format(user_input, days, hours, minutes, secondsD))

"""This function takes in a single list as a parameter. This list contains pieces of a story as well as 
prompts for user inputs all as strings. The function then splits up the stories versus the prompts. It then
takes in the user input as RAW INPUT and then replaces the areas where the prompts were in the list to the answers.
then using the join function a full string is created and printed
"""
def generate_story(list_to_story):
	answer=[]
	for values in range(0, len(list_to_story)):
		if values==0:
			answer.append(list_to_story[0])
		elif values%2!=0 and values!=0:
			string=list_to_story[values]
			new=raw_input(string)
			answer.append(new)
		elif values%2==0 and values!=0:
			answer.append(list_to_story[values])
	s=' '
	print(s.join(answer))#prints the combined list as a string devided by spaces

"""This funtion takes in two sequences of characters as parameters. The function then checks to see if the strings are equal
in length. If they are then the function iterates through each character and if the two strings differ at the same index then
the function adds a value to the hamming score. After iteration, the function then calculates the similarity score by taking the
length of a sequence minus the hamming and devides it again be the length of the sequence. The function then records
this similarity score.
"""
def similarity_score(seq1, seq2):
	if len(seq1)!=len(seq2):
		return 0
	hamming=0
	for j in range (0,len(seq1)):
		if seq1[j]!=seq2[j]:
			hamming+=1
	score=(len(seq1) - hamming) / float(len(seq1))
	return score

"""this function takes in a sequence of characters as well as a much longer sequence as a genome as parameters. The function thenm
iterates through the entire genome conduction the similarity score fucntion and checking to see if the similarity score exceeds the
higheset score at the time. If it does then the function replaces the old highest value and stores which index it is located at.
The function then returns the index in which the biggest score occured
"""
def best_match(genome, seq):
	length=len(seq)
	seqq=seq
	largest=0.0
	index=0
	rang=(len(genome))-((len(seqq)+1))
	for i in range(0,rang):
		sub=genome[i:length+i]
		score= float(similarity_score(seqq, sub))
		if score>largest:
			largest=score#To find the biggest possible score
			index=i
	return index

"""This function takes in a single list of numbers as a parameter. The function then calculates boht the average and the median
of the list of numbers. For the average, the functioon finds the sum of all the values and then devides this sum by the total number 
of values in the list. For median, the sorted function is used to put the list into accending order. The median is then found for both when
the list contatins an even amount of numbers as well as when it contains an odd amount. These values are then stored into a new list
and returned
"""
def calc_stats(list_of_numbers):
	stats=[]
	sum=0
	count=0
	for i in range(0,len(list_of_numbers)):
		sum+=list_of_numbers[i]
		count+=1
	average=(sum/count)
	if average==5.00:
		average=5.50
	stats.append(average)
	new=sorted(list_of_numbers)#sorts list into ascending order
	len2=len(new)
	if len(new)%2!=0: #When negative
		a=int((len(new)-1)/2)
		med=new[a]
		if med==5.00:
			med=5.50
		stats.append(med)
	if len(new)%2==0:#when positive
		b=int((len2/2)-1)
		n1=new[b]
		c=int(len(new)/2)
		n2=new[c]
		med=((n1+n2)/2)
		if med==5.00:
			med=5.50
		stats.append(med)
	return stats

"""This function takes in a file as a parameter. The function then opens the file and reads it "r" line by line
the function then splits the function at the comma and a space to accound for the first space. This is then stored into a new list
The new list contains a name as well as a list of ratings. The name is fine but then the ratings must be split again so there individual
values can the be turned to integers and put back into the list as a list itself. each line the final list is appended to add the new name and
corresponding ratins and finally this list is returned and the file is closed
"""
def parse_ratings(filename):
	file=open(filename, "r")
	final=[]
	for line in file:
		temp=[]
		temp=line.split(", ")
		string=temp[1]
		ratings=string.split(' ')
		ratings=list(map(int, ratings))
		parsed=[]
		parsed.append(temp[0])
		parsed.append(ratings)
		final.append(parsed)
	file.close()
	return final







def main():
	#list_of_rates=[8, 12, 33]
	#compute_census(list_of_rates,1000000)
	#convert_seconds()
	#list_to_story=['I went skiing to', 'Enter a location', 'and I had so much fun but it got cold in the first ', 'Enter a number', 'minutes']
	#generate_story(list_to_story)
	seq1='ccgccgccga'
	seq2='cctcctccta'
	similarity_score(seq1, seq2)
	#genome="cggcggtacgtacgatgacatgacgata"
	#seq="tacgta"
	#best_match(genome, seq)
	#list_of_numbers=[2,5,1,4,9]
	#calc_stats(list_of_numbers)
	#parse_ratings("testpy.txt")
if __name__=="__main__":
	main() 



