## Interface for CRUD operations on katas

import json
import subprocess

# def createKata(fileName: str, question: str, options: [str], correct: int) -> bool:
	# print("do stuff")
	# return true

def readKatas(fileName: str) -> dict:
	try:
		with open(fileName) as f:
			katas = json.load(f)
			return katas
	except Exception as e:
		subprocess.run(['bash', 'errLog.sh', 'readKatas failed with: ' + str(e)])
		return None

"""
def modifyKata(key: str, val: str) -> bool:
	try:
		with open(fileName) as f:
			katas = json.load(f)
			return true
	except Exception as e:
		subprocess.run(['bash', 'errLog.sh', 'modifyKata failed with: ' + str(e)])
		return false
"""


# optional args - either id or question
# def deleteKata(fileName: str, id: int)


