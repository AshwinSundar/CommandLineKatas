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
def test_read():
	katas = kataCrud.readKatas("test.json")["katas"]
	try:
		kata0 = katas[0]
		assert kata0["id"] == "0"
		assert kata0["question"] == "Is this the first kata?"
		assert kata0["opt1"] == "yes"
		assert kata0["opt2"] == "no"
		assert kata0["correct"] == "1"
		results["test_read"] = "true"
	except Exception as e:
		print(e)
		results["test_read"] = "false"
####


## TEST EXECUTIONS	
test_read()

####

print_test_results(results)
