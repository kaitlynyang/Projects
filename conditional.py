print ("A girl is walking down the street. A stranger offers her a piece of candy.")
candy = input ("Does she take the candy?") 
if candy == "yes":
	print ("The stranger gives her the candy and asks if she wants to get in his car.")
	car = input ("Does she get into the car?")
	if car == "yes" :
		print ("The stranger takes her to his house, and makes her work for him.")
		work = input ("Does she run away at night?")
		if work == "yes" :
			print ("She runs away from the stranger and goes home. The end!")
		else: 
			print ("The girl stays and works at the stranger's house.")
	else: 
		print ("The girl runs away from the stranger and goes home. The end!")
else:
	print ("The girl runs away from the stranger and goes home. The end!")
	
