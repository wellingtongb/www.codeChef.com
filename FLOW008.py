
testCase =int(raw_input("How many test do you want to do?"));

while testCase > 0:
	value = raw_input("If you are a good servant insert a number less tham 10: ")
	valueSplit = value.split(" ")
	finalResult = int(valueSplit[0])
	if(finalResult < 10):
		print "What an obedient servant you are!"
	else :
		print"-1"
	testCase -= 1

