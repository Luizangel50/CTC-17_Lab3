import math

def readData(data):
	"""Read each line of data files and add them to dictionary"""

	data["movies"] = {}
	data["users"] = {}
	data["ratings"] = {}

	# Iterates over lines of movies file and get data
	for line in open("../../data/movies.dat", "r"):
		elements = line.split("::")

		data["movies"][elements[0]] = {}
		data["movies"][elements[0]]["title"] = elements[1]
		data["movies"][elements[0]]["genres"] = elements[2].replace("\n", "").split("|")

	
	# Iterates over lines of users file and get data
	for line in open("../../data/users.dat", "r"):
		elements = line.split("::")

		data["users"][elements[0]] = {}
		data["users"][elements[0]]["gender"] = elements[1]
		data["users"][elements[0]]["age"] = elements[2]
		data["users"][elements[0]]["occupation"] = elements[3]
		data["users"][elements[0]]["zip_code"] = elements[4].replace("\n", "")


	# Iterates over lines of ratings file and get data
	for line in open("../../data/ratings.dat", "r"):
		elements = line.split("::")

		data["ratings"][elements[0], elements[1]] = {}
		data["ratings"][elements[0], elements[1]]["rating"] = elements[2]
		data["ratings"][elements[0], elements[1]]["timestamp"] = elements[3].replace("\n", "")