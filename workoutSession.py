import datetime

class workoutSession:
	def __init__(self, year, month, date, routine, note):
		self.date = datetime.datetime(year, month, date)
		self.routine = routine
		self.note = note

# -------------------------- Testing for workoutSession Class --------------------------
# ------------------------------------------------------------------------------
testWorkoutSession = workoutSession(2021, 3, 6, "Push", "I only completed half the reps for the last set of bench press")
print(testWorkoutSession.routine)
print(testWorkoutSession.date)
print(testWorkoutSession.note)