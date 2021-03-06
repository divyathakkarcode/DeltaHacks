import calendar

class Person:
	def __init__(self, username, age, weight, personalRoutines, workoutHistory):
		self.username = username
		self.age = age
		self.weight = weight
		self.personalRoutines = personalRoutines

class Routine:
	def __init__(self, routineName, exercisesArray, targetReps):
		self.routineName = routineName
		self.exercisesArray = exercisesArray
		self.targetReps = targetReps
		# not user friendly, fix this
	
	# ADD FUNCTION def editReps
	# ADD FUNCTION def addExercise
	def addExercise (self,exercisesArray,targetReps, newExercise, newReps):
                

'''
# -------------------------- Testing for Routine Class --------------------------
# ------------------------------------------------------------------------------
pushRoutine = Routine("Push", ["Push Ups", "Bench Press", "Shoulder Press"], [25, 8, 5])
# print(pushRoutine.routineName)
# print(pushRoutine.exercisesArray)
# print(pushRoutine.targetReps)

pullRoutine = Routine("Pull", ["Pull Ups", "Deadlifts", "Bicep Curls"], [10, 8, 16])
# print(pullRoutine.routineName)
# print(pullRoutine.exercisesArray)
# print(pullRoutine.targetReps)

legsRoutine = Routine("Legs", ["Squats", "Lunges", "Glute Bridges"], [30, 10, 6])
# print(legsRoutine.routineName)
# print(legsRoutine.exercisesArray)
# print(legsRoutine.targetReps)

# -------------------------- Testing for Person Class --------------------------
# ------------------------------------------------------------------------------
testUser = Person("MrKanister12", 20, 140, [pushRoutine, pullRoutine, legsRoutine])
print(testUser.username)
print(testUser.age)
print(testUser.weight)
print(testUser.personalRoutines[0].routineName)
print(testUser.personalRoutines[0].exercisesArray)
print(testUser.personalRoutines[0].targetReps)
print(testUser.personalRoutines[1].routineName)
print(testUser.personalRoutines[1].exercisesArray)
print(testUser.personalRoutines[1].targetReps)
print(testUser.personalRoutines[2].routineName)
print(testUser.personalRoutines[2].exercisesArray)
print(testUser.personalRoutines[2].targetReps)
'''
