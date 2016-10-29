from __future__ import division
from helper import readData
from time import time
from random import randint

def main():
	"""Main function"""

	print "----------------------- A PRIORI CLASSIFIER -----------------------"
	start_time = time()
	data = {}

	readData(data)

	aPrioriClassifier(data)

	testCase(data)

	print
	print "Execution time:", time() - start_time

def aPrioriClassifier(data):
	"""Function that classify each movie based on A Priori Classifier"""

	# Iterate over the ratings to get the sum of scores for each movie
	for movieRating in data["ratings"]:

		data["movies"][movieRating[1]]["mean"] += int(data["ratings"][movieRating]["rating"])
		data["movies"][movieRating[1]]["ratings_quantity"] += 1

	# Iterate over the movies to get the mean for each movie
	# If there is not ratings in a movie, return a random score
	for movie in data["movies"]:

		if data["movies"][movie]["ratings_quantity"] != 0:
			data["movies"][movie]["mean"] = int(round(data["movies"][movie]["mean"]/data["movies"][movie]["ratings_quantity"], 0))
		else:
			data["movies"][movie]["mean"] = randint(1, 5)

def testCase(data):

	movies = ["32", "47", "73", "2959", "858", "924", "2010", "1097", "3910", "1219", "3578", "3623", "1997", "2124", "829", "1073", "2950", "1499", "1653", "1645", "1688", "1721"]

	for movie in movies:
		print data["movies"][movie]["title"], ":", data["movies"][movie]["mean"]


if __name__ == "__main__":
	main()