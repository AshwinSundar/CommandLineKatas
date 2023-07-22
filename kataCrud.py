## Interface for CRUD operations on katas

import json

# def createKata(fileName: str, question: str, options: [str], correct: int) -> bool:
	# print("do stuff")
	# return true

def readKatas(fileName: str) -> dict:
	f = open(fileName)
	katas = json.load(f)
	return katas

# optional args for each param
# def modifyKata(fileName: str, question: str, options: [str], correct: int) -> bool:
	# print("do stuff")
	# return true


# optional args - either id or question
# def deleteKata(fileName: str, id: int)


