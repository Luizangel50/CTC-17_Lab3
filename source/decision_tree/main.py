from __future__ import division
from math import log
from helper import readData
from classes import Lists, NodeTree
from sys import float_info
from time import time


def main():
	"""Main function"""

	print "----------------------- DECISION TREE CLASSIFIER -----------------------"
	start_time = time()
	data = {}

	# Reading data from input files
	readData(data)

	listRatings = Lists

	# List of attributes that will be considered to build the decision tree
	attrs = ["genders", "ages", "occupations", "genres"]

	# Creating the root node
	initial_node = NodeTree(None, "root", None)

	# Calling the recursive function that builds the decision tree
	relativeEntropy(data, data["ratings"], attrs, listRatings, initial_node)

	# Decision tree leaves debug
	# printLeaves(initial_node)

	# Call the test case
	testCase(data, initial_node)

	print "\nExecution time:", time() - start_time, "seg"


def oneAttributeEntropy(innerPortion, innerTotal, lists):
	"""Calculates the partial entropy of a given attribute"""

	innerEntropy = 0

	for numberRating in lists.ratings.keys():
		if innerPortion[numberRating] != 0:
			portion = innerPortion[numberRating]/innerTotal
			innerEntropy += -portion*log(portion, 2)

	return innerEntropy

def relativeEntropy(data, selected_ratings, attributes, lists, decisionTree_node):
	"""Calculates the entropy of a given attribute"""

	totalRatings = len(selected_ratings)

	entropies = {}

	# For each attribute on the list, calculate the entropy based on the inputed ratings
	for attribute in attributes:

		partialEntropy = 0
		
		if attribute in ["genders", "ages", "occupations"]:
			for element in eval("lists." + attribute):
				
				innerPortion = {}
				innerTotal = 0
				innerEntropy = 0
				for numberRating in lists.ratings.keys():
					innerPortion[numberRating] = 0
					for rating in [item for item in selected_ratings if selected_ratings[item]["rating"] == numberRating]:
						if data["users"][rating[0]][attribute[:-1]] == element:
							innerPortion[numberRating] += 1

					innerTotal += innerPortion[numberRating]

				innerEntropy = oneAttributeEntropy(innerPortion, innerTotal, lists)
				partialEntropy += (innerTotal/totalRatings)*innerEntropy

		elif attribute == "genres":
			for genre in lists.genres:

				innerPortion = {}
				innerTotal = 0
				innerEntropy = 0
				for numberRating in lists.ratings.keys():
					innerPortion[numberRating] = 0
					for rating in [item for item in selected_ratings if selected_ratings[item]["rating"] == numberRating]:
						if genre in data["movies"][rating[1]]["genres"]:
							innerPortion[numberRating] += 1

					innerTotal += innerPortion[numberRating]

				innerEntropy = oneAttributeEntropy(innerPortion, innerTotal, lists)
				partialEntropy += (innerTotal/totalRatings)*innerEntropy

		entropies[attribute] = partialEntropy

	
	minorEntropy = {
		"attribute" : None,
		"value" : float_info.max
	}

	# Selected the attribute with minor entropy
	for entropy_key in entropies:
		if entropies[entropy_key] < minorEntropy["value"]:
			minorEntropy["attribute"] = entropy_key
			minorEntropy["value"] = entropies[entropy_key]

	# Remove the attribute with minor entropy of the attributes list
	new_attributes = list(attributes)
	new_attributes.remove(minorEntropy["attribute"])
	
	# For each value of choosen attribute, select new data with that feature
	# and expand in depth the decision tree
	for child in eval("lists." + minorEntropy["attribute"]):
		new_ratings = {}

		if minorEntropy["attribute"] in ["genders", "ages", "occupations"]:
			for item in selected_ratings:
				if data["users"][item[0]][minorEntropy["attribute"][:-1]] == child:
					new_ratings[item] = selected_ratings[item]
		elif minorEntropy["attribute"] == "genres":
			for item in selected_ratings:
				if child in data["movies"][item[1]]["genres"]:
					new_ratings[item] = selected_ratings[item]


		if new_attributes and new_ratings:
			new_node = NodeTree(decisionTree_node, minorEntropy["attribute"], child)
			decisionTree_node.children.append(new_node)
			relativeEntropy(data, new_ratings, new_attributes, lists, new_node)
		elif not new_attributes and new_ratings:
			mean_rating = {
				"ratings": 0,
				"quantity": 0
			}
			for numberRating in new_ratings:
				mean_rating["ratings"] += int(new_ratings[numberRating]["rating"])
				mean_rating["quantity"] += 1

			mean_rating["ratings"] = int(round(mean_rating["ratings"]/mean_rating["quantity"]))

			leaf_node = NodeTree(decisionTree_node, "ratings", mean_rating["ratings"])
			decisionTree_node.children.append(leaf_node)


def testCase(data, node):
	"""Function that implement a test based on my information"""

	user_info = {
		"gender" : "M",
		"age" : "18",
		"occupation": "4",
	}

	movies = ["32", "47", "73", "2959", "858", "924", "2010", "1097", "3910", "1219", "3578", "3623", "1997", "2124", "829", "1073", "2950", "1499", "1653", "1645", "1688", "1721"]
	genres = []
	for movie in movies:
		genres = list(data["movies"][movie]["genres"])
		rates = []
		treeSearch(node, user_info, genres, rates)
		mean = 0
		
		for rate in rates:
			mean += int(rate)
		mean = int(round(mean/len(rates), 0))

		print data["movies"][movie]["title"], ":", mean		


def treeSearch(node, user_info, genres, rates):
	"""Function that searches ratings on the decision tree"""


	if node.attribute == "ratings":
		rates.append(node.value_attribute)
	elif node.attribute == "root":
		for child in node.children:
			if child.attribute == "ratings":
				treeSearch(child, user_info, genres, rates)
			elif child.value_attribute == user_info[child.attribute[:-1]]:
				treeSearch(child, user_info, genres, rates)
				break
	else:
		for child in node.children:

			if child.attribute == "ratings":
				treeSearch(child, user_info, genres, rates)
			elif child.attribute != "genres" and child.value_attribute == user_info[child.attribute[:-1]]:
				treeSearch(child, user_info, genres, rates)
			elif child.attribute == "genres":
				for genre in child.value_attribute:
					if genre in genres:
						treeSearch(child, user_info, genres, rates)


def printLeaves(node):
	"""Print the decision tree's leaves information for debug"""
	
	if not node.children:
		print node.attribute, ":", node.value_attribute

	for child in node.children:
		printLeaves(child)


if __name__ == "__main__":
	main()