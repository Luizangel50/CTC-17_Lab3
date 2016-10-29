class Lists:
	"""Represents lists and maps of attibutes"""

	genders = ["M", "F"]
	ages = [
		"1",
		"18",
		"25",
		"35",
		"45",
		"50",
		"56",
	]

	occupations = [
		"0",
		"1",
		"2",
		"3",
		"4",
		"5",
		"6",
		"7",
		"8",
		"9",
		"10",
		"11",
		"12",
		"13",
		"14",
		"15",
		"16",
		"17",
		"18",
		"19",
		"20",
	]

	genres = [
		"Action",
		"Adventure",
		"Animation",
		"Children's",
		"Comedy",
		"Crime",
		"Documentary",
		"Drama",
		"Fantasy",
		"Film-Noir",
		"Horror",
		"Musical",
		"Mystery",
		"Romance",
		"Sci-Fi",
		"Thriller",
		"War",
		"Western",
	]

	ratings = {
		"1": {},
		"2": {},
		"3": {},
		"4": {},
		"5": {},
	}

# class Movie:
# 	"""Class that represents a movie"""

# 	def __init__(self, elements):
# 		"""Constructor"""

# 		self.movieID = elements[0]
# 		self.title = elements[1]
# 		self.genres = elements[2].replace("\n", "").split("|")

# class User:
# 	"""Class that represents a user"""

# 	def __init__(self, elements):
# 		"""Constructor"""

# 		self.userID = elements[0]
# 		self.gender = elements[1]
# 		self.age = elements[2]
# 		self.occupation = elements[3]
# 		self.zip_code = elements[4]

# class Rating:
# 	"""Class that represents a rating"""

# 	def __init__(self, elements):
# 		"""Constructor"""

# 		self.userID = elements[0]
# 		self.movieID = elements[1]
# 		self.rating = elements[2]
# 		self.timestamp = elements[3]


# class Statistics:
# 	"""Class that represents statistics about the number of users
# 	for each classification"""

# 	def __init__(self):
# 		"""Constructor"""

# 		self.rating1 = 0
# 		self.rating2 = 0
# 		self.rating3 = 0
# 		self.rating4 = 0
# 		self.rating5 = 0

# 	def __iter__(self):
# 		"""returns a dictionary with attibutes names and its values"""

# 		for attr, value in self.__dict__.iteritems():
# 			yield attr, value

# 	def __len__(self):
# 		"""returns the number of attributes of this class"""

# 		return len(dict(self))


class NodeTree(object):
	"""Class that describes a tree node"""

	def __init__(self, parent_node, attribute, value_attribute): #, selected_data):
		"""Constructor"""

		self.parent_node = parent_node
		self.attribute = attribute
		self.value_attribute = value_attribute
		self.children = []
		