import datetime

class Person:
	def __init__(self, username, age, weight, personalRoutines, workoutHistoryArray):
		self.username = username
		self.age = age
		self.weight = weight
		self.personalRoutines = personalRoutines
		self.workoutHistoryArray = []

	# Accessors
	def getUsername(self):
		return self.username

	def getAge(self):
		return self.age

	def getWeight(self):
		return self.weight

	def getPersonalRoutines(self):
		return self.personalRoutines

	def getworkoutHistoryArray(self):
		return self.workoutHistoryArray

	# Mutators
	
	def editUsername(self, updatedUsername):
		self.username = updatedUsername

	def editAge(self, updatedAge):
		self.age = updatedAge

	def editWeight(self, updatedWeight);
		self.weight = updatedWeight

	def addPersonalRoutine(self, addedRoutine):
		self.personalRoutines.append(addedRoutine)

	def deletePersonalRoutine(self, deletedRoutineName):
		isDeletionComplete = False

		for routine in self.personalRoutines:
			if(routine.routineName == deletedRoutineName):
				self.personalRoutines.remove(routine)
				isDeletionComplete = True
		
		if(isDeletionComplete == False):
			print("This routine could not be found and was not deleted")

	# Might need to call the constructor of the workoutSession class to actually create a workoutSession object that gets added to the workoutHistoryArray
	# On second thought, this should be fine since we can call constructor of workoutSession then add that addedSession to a user's workoutHistoryArray
	def addWorkoutSession(self, addedSession):
		self.workoutHistoryArray.append(addedSession)

	# Assumed that only one workoutSession is entered per day and a session can be referenced by a specific date
	def deleteWorkoutSession(self, deletedSessionYear, deletedSessionMonth, deletedSessionDayOfMonth):
		isDeletionComplete = False

		for session in self.workoutHistoryArray:
			deletedDate = datetime.datetime(deletedSessionYear, deletedSessionMonth, deletedSessionDayOfMonth)
			if(session.date == deletedDate):
				self.workoutHistoryArray.remove(session)
				isDeletionComplete = True
		
		if(isDeletionComplete == False):
			print("No workout session with this date could be found and no deletion occured")

class workoutSession:
	def __init__(self, year, month, dayOfMonth, routine, note):
		self.date = datetime.datetime(year, month, dayOfMonth)
		self.routine = routine
		self.note = note

	# Accessors
	def getDate(self):
		return self.date

	def getRoutine(self):
		return self.routine

	def getNote(self):
		return self.note

	# Mutators
	def editDate(self, updatedYear, updatedMonth, updatedDayOfMonth):
		self.date = datetime.datetime(updatedYear, updatedMonth, updatedDayOfMonth)
	
	def editNote(self, updatedNote):
		self.note = updatedNote

class Routine:
	def __init__(self, routineName, exercisesArray, targetRepsArray, targetSetsArray):
		self.routineName = routineName
		self.exercisesArray = exercisesArray
		self.targetRepsArray = targetRepsArray
		self.targetSetsArray = targetSetsArray
		# not user friendly way to initiate with, maybe use a 3D array or a dictionary if it makes things easier

	# Accessors
	def getRoutineName(self):
		return self.routineName

	def getExercisesArray(self):
		return self.exercisesArray

	def gettargetRepsArray(self):
		return self.targetRepsArray

	def gettargetSetsArray(self):
		return self.targetSetsArray

	# Mutators
	def edittargetRepsArray(self, updatedtargetRepsArray):
		self.targetRepsArray = updatedtargetRepsArray
	
	def edittargetSetsArray(self, updatedtargetSetsArray):
		self.targetSetsArray = updatedtargetSetsArray

	def editRoutineName(self, updatedRoutineName):
		self.routineName = updatedRoutineName

	def addExercise (self, newExercise, newReps, newSets):
		
		if newExercise not in self.exercisesArray:
			self.exercisesArray.append(newExercise)
			self.targetRepsArray.append(newReps)
			self.targetSetsArray.append(newSets)
		else:
			print("This exercise already exists within the routine")

	def deleteExercise(self, targetRoutine, deletedExercise):
		try:
			deletedIndex = targetRoutine.exercisesArray.index(deletedExercise)
		except ValueError:
			print("This exercise is not in the routine")

		targetRoutine.exercisesArray.pop(deletedIndex)
		targetRoutine.targetRepsArray.pop(deletedIndex)
		targetRoutine.targetSetsArray.pop(deletedIndex)

# -------------------------- Testing for Person Class --------------------------
# ------------------------------------------------------------------------------
testUser = Person("MrKanister12", 20, 140, [pushRoutine, pullRoutine, legsRoutine], [])
print(testUser.username)
print(testUser.age)
print(testUser.weight)
print(testUser.personalRoutines[0].routineName)
print(testUser.personalRoutines[0].exercisesArray)
print(testUser.personalRoutines[0].targetRepsArray)
print(testUser.personalRoutines[1].routineName)
print(testUser.personalRoutines[1].exercisesArray)
print(testUser.personalRoutines[1].targetRepsArray)
print(testUser.personalRoutines[2].routineName)
print(testUser.personalRoutines[2].exercisesArray)
print(testUser.personalRoutines[2].targetRepsArray)



# -------------------------- Testing for Routine Class --------------------------
# ------------------------------------------------------------------------------
pushRoutine = Routine("Push", ["Push Ups", "Bench Press", "Shoulder Press"], [25, 8, 5], [3, 3, 3])
# print(pushRoutine.routineName)
# print(pushRoutine.exercisesArray)
# print(pushRoutine.targetRepsArray)
# print(pushRoutine.targetSetsArray)

pullRoutine = Routine("Pull", ["Pull Ups", "Deadlifts", "Bicep Curls"], [10, 8, 16], [4, 4, 4])
# print(pullRoutine.routineName)
# print(pullRoutine.exercisesArray)
# print(pullRoutine.targetRepsArray)
# print(pushRoutine.targetSetsArray)

legsRoutine = Routine("Legs", ["Squats", "Lunges", "Glute Bridges"], [30, 10, 6], [5, 5, 5])
# print(legsRoutine.routineName)
# print(legsRoutine.exercisesArray)
# print(legsRoutine.targetRepsArray)
# print(pushRoutine.targetSetsArray)

# -------------------------- Testing for addExercise Method --------------------------
# ------------------------------------------------------------------------------
pushRoutine.addExercise("Dips", 10, 4)
pushRoutine.deleteExercise("Dips", 10, 4)
print(pushRoutine.exercisesArray)
print(pushRoutine.targetRepsArray)
print(pushRoutine.targetSetsArray)




# -------------------------- Testing for workoutSession Class --------------------------
# ------------------------------------------------------------------------------
testWorkoutSession = workoutSession(2021, 3, 6, pushRoutine, "I only completed half the reps for the last set of bench press")
print(testWorkoutSession.routine.routineName)
print(testWorkoutSession.date)
print(testWorkoutSession.note)