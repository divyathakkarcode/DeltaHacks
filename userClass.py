import calendar

class workoutSession:
	def __init__(self, calendar.date, personalRoutine, 

class Routine:
	def __init__(self, routineName, exercisesArray, repsArray):
		self.routineName = routineName
		self.exercisesArray = exercisesArray
		self.repsArray = repsArray

class Person:
	def __init__(self, username, age, weight, personalRoutines):
		self.username = username
		self.age = age
		self.weight = weight
		self.personalRoutines = personalRoutines
	
	def createPersonalRoutines():

testUser = Person("MrKanister12", 20, 140, [ ["Pull", ["Pull Ups", "Deadlift"]], ["Push", ["Benchpress", "Pushups"]], ["Legs", ["Squats", "Lunges"]] ])
print(testUser.username)
print(testUser.age)
print(testUser.weight)
print(testUser.personalRoutines)
print(testUser.personalRoutines[0])
print(testUser.personalRoutines[1])
print(testUser.personalRoutines[2])

testUser = fitnessUser("MrKanister12", 20, 140, [ ["Pull", ["Pull Ups", "Deadlift"]], ["Push", ["Benchpress", "Pushups"]], ["Legs", ["Squats", "Lunges"]] ])
print(testUser.username)
print(testUser.age)
print(testUser.weight)
print(testUser.personalRoutines)
print(testUser.personalRoutines[0])
print(testUser.personalRoutines[1])
print(testUser.personalRoutines[2])
