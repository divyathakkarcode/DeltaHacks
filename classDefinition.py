import datetime
# ADD ACCESSORS FOR ALL CLASSES AND ALL PARAMETERS

class Person:
	def __init__(self, username, age, weight, personalRoutines, workoutHistory):
		self.username = username
		self.age = age
		self.weight = weight
		self.personalRoutines = personalRoutines

	def getAge(self):
		return self.age

	# ADD METHOD TO ADD WORKOUT SESSION
	# ADD METHOD TO DELETE SESSION

class workoutSession:
	def __init__(self, year, month, date, routine, note):
		self.date = datetime.datetime(year, month, date)
		self.routine = routine
		self.note = note

	# ADD METHOD TO EDIT DATE, NOTE_,

class Routine:
	def __init__(self, routineName, exercisesArray, targetReps, targetSets):
		self.routineName = routineName
		self.exercisesArray = exercisesArray
		self.targetReps = targetReps
		self.targetSets = targetSets
		# not user friendly, fix this
	
	# ADD FUNCTION def edit targetReps
	# ADD FUNCTION def edit targetSets
	# ADD FUNCTION def delete exercise
	# ADD FUNCTION edit routineName
	def addExercise (self, newExercise, newReps, newSets):
                self.exercisesArray.append(newExercise)
                self.targetReps.append(newReps)
                self.targetSets.append(newSets)
#hello



# -------------------------- Testing for Routine Class --------------------------
# ------------------------------------------------------------------------------
pushRoutine = Routine("Push", ["Push Ups", "Bench Press", "Shoulder Press"], [25, 8, 5], [3, 3, 3])
# print(pushRoutine.routineName)
# print(pushRoutine.exercisesArray)
# print(pushRoutine.targetReps)
# print(pushRoutine.targetSets)

pullRoutine = Routine("Pull", ["Pull Ups", "Deadlifts", "Bicep Curls"], [10, 8, 16], [4, 4, 4])
# print(pullRoutine.routineName)
# print(pullRoutine.exercisesArray)
# print(pullRoutine.targetReps)
# print(pushRoutine.targetSets)

legsRoutine = Routine("Legs", ["Squats", "Lunges", "Glute Bridges"], [30, 10, 6], [5, 5, 5])
# print(legsRoutine.routineName)
# print(legsRoutine.exercisesArray)
# print(legsRoutine.targetReps)
# print(pushRoutine.targetSets)

# -------------------------- Testing for addExercise Method --------------------------
# ------------------------------------------------------------------------------
pushRoutine.addExercise("Dips", 10, 4)
print(pushRoutine.exercisesArray)
print(pushRoutine.targetReps)
print(pushRoutine.targetSets)

# -------------------------- Testing for Person Class --------------------------
# ------------------------------------------------------------------------------
testUser = Person("MrKanister12", 20, 140, [pushRoutine, pullRoutine, legsRoutine], [])
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

# -------------------------- Testing for workoutSession Class --------------------------
# ------------------------------------------------------------------------------
testWorkoutSession = workoutSession(2021, 3, 6, pushRoutine, "I only completed half the reps for the last set of bench press")
print(testWorkoutSession.routine.routineName)
print(testWorkoutSession.date)
print(testWorkoutSession.note)