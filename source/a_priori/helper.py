import math

def readData(data):
	"""Read each line of data files and add them to dictionary"""

	data["movies"] = {}
	data["ratings"] = {}

	# Iterates over lines of movies file and get data
	for line in open("../../data/movies.dat", "r"):
		elements = line.split("::")

		data["movies"][elements[0]] = {}
		data["movies"][elements[0]]["title"] = elements[1]
		data["movies"][elements[0]]["genres"] = elements[2].replace("\n", "").split("|")
		data["movies"][elements[0]]["mean"] = 0
		data["movies"][elements[0]]["ratings_quantity"] = 0


	# Iterates over lines of ratings file and get data
	for line in open("../../data/ratings.dat", "r"):
		elements = line.split("::")

		data["ratings"][elements[0], elements[1]] = {}
		data["ratings"][elements[0], elements[1]]["rating"] = elements[2]
		data["ratings"][elements[0], elements[1]]["timestamp"] = elements[3].replace("\n", "")