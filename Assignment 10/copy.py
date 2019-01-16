# CS1300 Fall 2017
# Author: 
# Recitation: 
# Assignment 10

import itertools as it


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

def lookup_average_rating(index, bookdict, avgdict):
	book=bookdict[index]
	title=book[0]
	title=title.strip("\n")
	author=book[1]
	lookup ="({}) {} by {}".format(avgdict[index],title,author)
	return lookup

#PART_2 follow here


class Recommender:
	def __init__(self, book_file_name, user_file_name):
		self.booklist=[]
		self.userdictionary={}
		self.averagelist=[]
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
			temp=[]
			temp1=[]
			temp=line.split(',')
			temp1.append(temp[1])
			temp1.append(temp[0])
			self.booklist.append(temp1)
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
			self.userdictionary[string]=rate
		"""
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
			for i in range(0,len(temp)):
				rate.append(int(temp[i]))
			string=temp1
			self.userdictionary[string]=rate
			"""
		return None

	def calculate_average_rating(self):
		sum = 0
		count = 0
		length = 0

		for key in self.userdictionary:
			tempratings = self.userdictionary[key]
			length = len(tempratings)

		for i in range(length):
			for key in self.userdictionary:
				tempratings = self.userdictionary[key]
				#print tempratings[i]
				if tempratings[i] != 0:
					sum = float(sum + tempratings[i])
					count = count+1
			self.averagelist.append(sum/count)
			sum = 0
			count = 0
		"""
		rateuser=[]
		sum=0
		count=0
		values=list(self.userdictionary.values())
		for i in range(0,len(values)):
			tempo=values[i]
			for j in range(0,len(tempo)):
				if tempo[j]!=0:
					sum+=tempo[j]
					count+=1
			av=round(sum/count, 2)
			sum=0
			count=0
			self.averagelist.append(av)
			"""
		return None

	def lookup_average_rating(self, book_index):
		book=self.booklist[book_index]
		title=book[0]
		title=title.strip("\n")
		author=book[1]
		lookup ="({}) {} by {}".format(self.averagelist[book_index],title,author)
		return lookup

	def calc_similarity(self, user1, user2):
		u1=self.userdictionary[user1]
		u2=self.userdictionary[user2]
		similarity_measure=0
		for i in range (0, len(u1)):
			product=u1[i]*u2[i]
			similarity_measure+=product
		return similarity_measure

	def get_most_similar_user(self, current_user_id):
		keys=list(self.userdictionary.keys())
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

	def recommend_books(self, current_user_id):
		recommendations_list=[]
		simuser=self.get_most_similar_user(current_user_id)
		userlist=self.userdictionary[simuser]
		currentuser=self.userdictionary[current_user_id]
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