import kataCrud

## TESTING UTILITIES
results = dict()

def print_test_results(res: dict):
	total = len(res.keys())
	passed = sum(r == "true" for r in res.values())
	failed = total - passed
	print(str(passed) + " PASSED")
	print(str(failed) + " FAILED")
	print(res)
#####
	

## TESTS
## checks contents
def test_read1():
	try:
		katas = kataCrud.readKatas("test.json")["katas"]
		kata0 = katas[0]
		assert kata0["id"] == "0"
		assert kata0["question"] == "Is this the first kata?"
		assert kata0["opt1"] == "yes"
		assert kata0["opt2"] == "no"
		assert kata0["correct"] == "1"
		results["test_read"] = "true"
	except Exception as e:
		print(e)
		results["test_read1"] = "false"

## tests read behavior
def test_read2():
	try:
		kata = kataCrud.readKatas("fileNotExist.json")["katas"]
		results["test_read2"] = "false"
	except Exception as e:
		results["test_read2"] = "true"
	
def test_read3():
	try:
		kata = kataCrud.readKatas("test.json")["invalidKey"]
		results["test_read3"] = "false"
	except Exception as e:
		results["test_read3"] = "true"
####


## TEST EXECUTIONS	
test_read1()
test_read2()
test_read3()

####

print_test_results(results)
