'''CS1300 Fall 2017
Author: JC Abrahamson
Recitation: 8 am on thursdays
Assignment 10'''


#PART_1 functions here
'''
This function takes a file of different books and authors as a parameter.
It reads the file and returns a list of each book and author that was in the file.
'''
def read_books(file_name):
	books = []
	try:
		f = open(file_name)
		for line in f:
			mylist = line.split(",")
			tempstr1 = mylist[0].strip().strip('\n')
			tempstr2 = mylist[1].strip().strip('\n')
			templist = []
			#print mylist
			templist.append(tempstr2)
			templist.append(tempstr1)
			books.append(templist)
		return books

	except:
		return None

'''
This function takes a file of different users and book ratings as a parameter.
It reads the file and returns a dictionary with the users' name as the key and
a list of ratings converted to integers as the value.
'''
def read_users(user_file):
	users = {}
	try:
		f = open(user_file)

		for line in f:
			mylist = line.split()
			#print mylist
			key = mylist[0]
			#print key
			tempvalues = []

			for i in range (1, len(mylist)):
				tempvalues.append(int(mylist[i]))

			users[key] = tempvalues

		return users

	except:
		return None

'''
This function takes a dictionary of users as keys and a list of book ratings as values
as a parameter. It calculates the average rating of every book by looping through the
values from the dictionary. It returns a list of the average rating of every book.
'''
def calculate_average_rating(ratings_dict):

	averages = []
	sum = 0
	count = 0
	length = 0

	for key in ratings_dict:
		tempratings = ratings_dict[key]
		length = len(tempratings)

	for i in range(length):
		for key in ratings_dict:
			tempratings = ratings_dict[key]
			#print tempratings[i]
			if tempratings[i] != 0:
				sum = float(sum + tempratings[i])
				count = count+1
		averages.append(sum/count)
		sum = 0
		count = 0

	return averages

'''
This function takes an index, a dictionary of users as keys and a list of
book ratings as values, and a list of the average ratings of each book as a
parameter. It returns a string with a certain book, the author, and the rating
of the book depending on what index value is passed in.
'''
def lookup_average_rating(index, book_dict, avg_ratings_dict):
	rating = avg_ratings_dict[index]
	bookname = book_dict[index][0]
	author = book_dict[index][1]

	#return  "("+rating+")"+bookname+" by "+author
	return  "(%.2f) %s by %s" %(rating,bookname, author)


#PART_2 follow here
class Recommender:
    #Constructor here
    '''
	This constructor takes a filename of books and a filename of users and ratings.
	It initializes a book list, user dictionary, and average rating list using the
	filenames and calling the above function.
	'''
	def __init__(self, books_filename, ratings_filename):
		self.book_list = []
		self.user_dictionary = {}
		self.average_rating_list = []

		self.book_list = read_books(books_filename)
		self.user_dictionary = read_users(ratings_filename)
		self.average_rating_list = calculate_average_rating(self.user_dictionary)

	'''

	'''
	def read_books(self, file_name):
		try:
			f = open(file_name)
			for line in f:
				mylist = line.split(",")
				tempstr1 = mylist[0].strip().strip('\n')
				tempstr2 = mylist[1].strip().strip('\n')
				templist = []
				templist.append(tempstr2)
				templist.append(tempstr1)
				self.book_list.append(templist)
		except:
			return None

	def read_users(self, file_name):
		try:
			f = open(user_file)

			for line in f:
				mylist = line.split()
				key = mylist[0]
				#print key
				tempvalues = []

				for i in range (1, len(mylist)):
					tempvalues.append(int(mylist[i]))

				self.user_dictionary[key] = tempvalues

		except:
			return None

	def calculate_average_rating(self):
		try:
			books = read_books("book.txt")
			sum = 0
			count = 0

			for i in range(len(books)):
				for key in ratings_dict:
					tempratings = ratings_dict[key]
					#print tempratings[i]
					if tempratings[i] != 0:
						sum = float(sum + tempratings[i])
						count = count+1
				self.average_rating_list.append(sum/count)
				sum = 0
				count = 0

		except:
			return None

	def lookup_average_rating(self, book_index):
		rating = self.average_rating_list[book_index]
		bookname = self.book_list[book_index][0]
		author = self.book_list[book_index][1]

		return  "(%.2f) %s by %s" %(rating,bookname, author)

"""
this function takes in 2 parameters being 2 users and it then finds the calculates the similarity score between the 2
users by multiplying their book ratings together and then summing this product. It then returns 
this score
"""
	def calc_similarity(self, user1, user2):
		similarity_measure = 0
		values1 = self.user_dictionary[user1]
		values2 = self.user_dictionary[user2]

		for i in range (len(values1)):
			similarity_measure = similarity_measure + values1[i]*values2[i]

		return similarity_measure

"""
This function takes in a single user as a parameter and then calculates the similarity score
betweent the user and all ofther users. If a similarity is greatere than all the previous ones it
replaces it as the largest score and returns this similarity score
"""
	def get_most_similar_user(self, current_user_id):
			#values = self.user_dictionary[current_user_id]
			comparison = 0
			best_user_match_id = ""

			for key in self.user_dictionary:
				if key != current_user_id:
					similaruser = key
					if comparison < self.calc_similarity(current_user_id, similaruser):
						comparison = self.calc_similarity(current_user_id, similaruser)
						best_user_match_id = similaruser

			return best_user_match_id
"""
This function also takes in a user as parameter and then finds the most similar user using the get most similar function
and with this user if then checks what book the similar user has rated 3 or 5 and that the current user did not rate (0)
and then calls the lookup function to display the book reccomendation
"""
	def recommend_books(self, current_user_id):
			recommendations_list = []
			similaruser = self.get_most_similar_user(current_user_id)

			userlist = self.user_dictionary[current_user_id]
			print userlist
			similaruserlist = self.user_dictionary[similaruser]
			print similaruserlist

			for i in range(len(userlist)):
				if similaruserlist[i] == 3 or similaruserlist[i] == 5:
					if userlist[i] == 0:
						recommendations_list.append(self.lookup_average_rating(i))

			return recommendations_list

def main():

	test = Recommender("book.txt", "ratings.txt")
	#print(test.lookup_average_rating(5))
	print(test.recommend_books("Ben"))
	print(test.get_most_similar_user("Ben"))
	users = read_users("ratings.txt")
	book = read_books("book.txt")
	average = calculate_average_rating(users)
	#print lookup_average_rating(0, book, average)
	#print read_books("book.txt")
	#print read_users("ratings.txt")
	#print calculate_average_rating(users)

if __name__ == "__main__":
	main()
