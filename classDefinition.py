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
	def editWeight(self, updatedWeight):
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
	# Edit these to be able to edit the reps of a single exercise by referencing its name (Ex. "Push Ups")
	# Also right now, if editTargetReps is used, the size of the array might not match the number of actual exercises in exercisesArray
	# So might need to add a check to make sure size of all arrays in this class are always equal
	def edittargetRepsArray(self, updatedtargetRepsArray):
		self.targetRepsArray = updatedtargetRepsArray
	
	# Edit these to be able to edit the sets of a single exercise by referencing its name (Ex. "Push Ups")
	# Also right now, if editTargetSets is used, the size of the array might not match the number of actual exercises in exercisesArray
	# So might need to add a check to make sure size of all arrays in this class are always equal
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

	def deleteExercise(self, deletedExercise):
		try:
			deletedIndex = self.exercisesArray.index(deletedExercise)
		except ValueError:
			print("This exercise is not in the routine")

		self.exercisesArray.pop(deletedIndex)
		self.targetRepsArray.pop(deletedIndex)
		self.targetSetsArray.pop(deletedIndex)
