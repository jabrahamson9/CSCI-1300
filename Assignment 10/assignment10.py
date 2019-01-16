# CS1300 Fall 2017
# Author: JC Abrahamson
# Recitation: 8 am thursday
# Assignment 10

import itertools as it # so i can do a two range for loop to ommit one index

'''
This function takes a file of different books and authors as a parameter.
It reads the file and returns a list of each book and author that was in the file.
'''
def read_books(filename):
	books=[]
	try:
		file=open(filename,"r")
	except IOError:
		return None
	if file==None:
		return []
	for line in file:
		temp=[]
		temp1=[]
		line=line.strip("\n")
		temp=line.split(',')
		temp1.append(temp[1])
		temp1.append(temp[0])
		books.append(temp1)
	return books

'''
This function takes a file of different users and book ratings as a parameter.
It reads the file and returns a dictionary with the users' name as the key and
a list of ratings converted to integers as the value.
'''
def read_users(userfilename):
	try:
		userfile=open(userfilename,"r")
	except IOError:
		return None
	if userfile==None:
		return {}
	d={}
	for line in userfile:
		temp=[]
		temp1=[]
		rate=[]
		string=""
		temp=line.split(' ')
		temp1=temp[0]
		temp.remove(temp[0])
		try:
			for i in range(0,len(temp)):
				rate.append(int(temp[i]))
		except ValueError:
			pass
		string=temp1
		d[string]=rate
	return d

'''
This function takes a dictionary of users as keys and a list of book ratings as values
as a parameter. It calculates the average rating of every book by looping through the
values from the dictionary. It returns a list of the average rating of every book.
'''
def calculate_average_rating(d):
	averages = []
	sum = 0
	count = 0
	length = 0

	for key in d:
		tempratings = d[key]
		length = len(tempratings)

	for i in range(length):
		for key in d:
			tempratings = d[key]
			#print tempratings[i]
			if tempratings[i] != 0:
				sum = float(sum + tempratings[i])
				count = count+1
		averages.append(sum/count)
		sum = 0
		count = 0
	print(averages)

	"""
	new=list(d.values())
	for i in range(0, len(d)):
		length=new[i]
		for j in range(0, len(length)):
			length[j]=float(length[j])
		new[i]=length
	rateuser=[]
	sum=0
	count=0
	averages=[]
	values=list(new)
	countlist=[0.0]*len(new[1])
	a=[0.0]*len(new[1])
	for i in range(0, len(a)):
		n=new[i]
		for j in range(0,len(n)):
			if n[j]!=0:
				a[j]+=n[j]
				countlist[j]+=1
	for i in range(0,len(a)):
		if countlist[i]!=0:
			posav= a[i]/countlist[i]
			st= '%.2f'%posav
			a[i]=float(st)
	averages=a
	print(a)
	"""
	return averages

'''
This function takes an index, a dictionary of users as keys and a list of
book ratings as values, and a list of the average ratings of each book as a
parameter. It returns a string with a certain book, the author, and the rating
of the book depending on what index value is passed in.
'''
def lookup_average_rating(index, bookdict, avgdict):
	book=bookdict[index]
	title=book[0]
	title=title.strip("\n")
	author=book[1]
	avdic='%.2f'%avgdict[index]
	lookup ="({}) {} by {}".format(avdic,title,author)
	return lookup

#PART_2 follow here

'''
This constructor takes a filename of books and a filename of users and ratings.
It initializes a book list, user dictionary, and average rating list using the
filenames and calling the above function.
'''
class Recommender:
	def __init__(self, book_file_name, user_file_name):
		self.book_list=[]
		self.user_dictionary={}
		self.avg_rating_list=[]
		self.read_books(book_file_name)
		self.read_users(user_file_name)
		self.calculate_average_rating()
	def read_books(self, file_name):
		try:
			file=open(file_name,"r")
		except IOError:
			return None
		if file==None:
			return []
		for line in file:
			line=line.strip("\n")
			temp=[]
			temp1=[]
			temp=line.split(',')
			temp1.append(temp[1])
			temp1.append(temp[0])
			self.book_list.append(temp1)
		return None

	def read_users(self, file_name):
		try:
			userfile=open(file_name,"r")
		except IOError:
			return None
		if userfile==None:
			return {}
		for line in userfile:
			temp=[]
			temp1=[]
			rate=[]
			string=""
			temp=line.split(' ')
			temp1=temp[0]
			temp.remove(temp[0])
			try:
				for i in range(0,len(temp)):
					rate.append(int(temp[i]))
			except ValueError:
				pass
			string=temp1
			self.user_dictionary[string]=rate
		return None

	def calculate_average_rating(self):
		sum = 0
		count = 0
		length = 0

		for key in self.user_dictionary:
			tempratings = self.user_dictionary[key]
			length = len(tempratings)

		for i in range(length):
			for key in self.user_dictionary:
				tempratings = self.user_dictionary[key]
				#print tempratings[i]
				if tempratings[i] != 0:
					sum = float(sum + tempratings[i])
					count = count+1
			self.avg_rating_list.append(sum/count)
			sum = 0
			count = 0

		return None

	def lookup_average_rating(self, book_index):
		book=self.book_list[book_index]
		title=book[0]
		title=title.strip("\n")
		author=book[1]
		dicav='%.2f'%self.avg_rating_list[book_index]
		lookup ="({}) {} by {}".format(dicav,title,author)
		return lookup

#this function takes in 2 parameters being 2 users and it then finds the calculates the similarity score between the 2
#users by multiplying their book ratings together and then summing this product. It then returns 
#this score
	def calc_similarity(self, user1, user2):
		u1=self.user_dictionary[user1]
		u2=self.user_dictionary[user2]
		similarity_measure=0
		for i in range (0, len(u1)):
			product=u1[i]*u2[i]
			similarity_measure+=product
		return similarity_measure

#This function takes in a single user as a parameter and then calculates the similarity score
#betweent the user and all ofther users. If a similarity is greatere than all the previous ones it
#replaces it as the largest score and returns this similarity score
	def get_most_similar_user(self, current_user_id):
		keys=list(self.user_dictionary.keys())
		high=0
		index=0
		ind=0
		for i in range(0,len(keys)):
			if keys[i]==current_user_id:
				ind=i
		for i in it.chain(range(0,ind-1), range(ind+1,len(keys))):
			number=self.calc_similarity(current_user_id,keys[i])
			if number>high:
				high=number
				index=i
		best_user_match_id=keys[index]
		return best_user_match_id

#This function also takes in a user as parameter and then finds the most similar user using the get most similar function
#and with this user if then checks what book the similar user has rated 3 or 5 and that the current user did not rate (0)
#and then calls the lookup function to display the book reccomendation
	def recommend_books(self, current_user_id):
		recommendations_list=[]
		simuser=self.get_most_similar_user(current_user_id)
		userlist=self.user_dictionary[simuser]
		currentuser=self.user_dictionary[current_user_id]
		for i in range(0,len(userlist)):
			if userlist[i]==3 and currentuser[i]==0:
				entry=self.lookup_average_rating(i)
				recommendations_list.append(entry)
		for i in range(0,len(userlist)):
			if userlist[i]==5 and currentuser[i]==0:
				entry=self.lookup_average_rating(i)
				recommendations_list.append(entry)
		return recommendations_list


def main():
	test=Recommender("book.txt","ratings.txt")
	test.read_books("book.txt")
	test.read_users("ratings.txt")
	test.calculate_average_rating()
	test.recommend_books("Ben")

if __name__ == "__main__":
    main()