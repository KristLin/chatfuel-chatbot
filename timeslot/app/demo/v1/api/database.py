import pickledb
import datetime
from random import randrange

# 'time' stands for 'timeslot'
# 'app'  stands for 'appointment'
timedb = 'timeslot.db'
appdb = 'appointment.db'


def get_default_timeslots():
	default_timeslots = {}
	for hour in range(9, 17):
		default_timeslots[str(hour) + '-' + str(hour + 1)] = False
	return default_timeslots


def get_coming_dates():
	dates = []
	for i in range(3):
		date = str(datetime.date.today() + datetime.timedelta(days=i+1)).split('-')
		date.reverse()
		date = '/'.join(date)
		dates.append(date)
	return dates


def check_date(date):
	date = date.split('/')
	# means the date is passed
	if datetime.date.today() > datetime.date(int(date[2]), int(date[1]), int(date[0])):
		return False
	return True


def generate_appointment_id():
	db = pickledb.load(appdb, True, False)
	appointment_ids = list(db.getall())
	while True:
		appointment_id = ''
		for _ in range(4):
			appointment_id += str(randrange(1, 9))
		if appointment_id not in appointment_ids:
			break
	return appointment_id


class TimeDB:
	@staticmethod
	def store(dname):
		db = pickledb.load(timedb, True, False)
		d_timeslots = {}
		coming_dates = get_coming_dates()
		default_timeslots = get_default_timeslots()
		for date in coming_dates:
			d_timeslots[date] = default_timeslots
		db.set(dname, d_timeslots)
		db.dump()

	@staticmethod
	def set(dname, date, hour, reserved=False):
		db = pickledb.load(timedb, True, False)
		d_timeslots = db.get(dname)
		d_timeslots[date][hour] = reserved
		db.set(dname, d_timeslots)
		db.dump()

	@staticmethod
	def get(dname):
		TimeDB.check_dates(dname)
		db = pickledb.load(timedb, True, False)
		d_timeslots = db.get(dname)
		for date in d_timeslots:
			for hour in d_timeslots[date]:
				if d_timeslots[date][hour]:
					d_timeslots[date][hour] = 'reserved'
				else:
					d_timeslots[date][hour] = 'available'
		return d_timeslots

	@staticmethod
	def get_available(dname):
		d_timeslots = TimeDB.get(dname)
		d_avialable = {}
		for date in d_timeslots:
			d_avialable[date] = []
			for hour in d_timeslots[date]:
				if d_timeslots[date][hour] == 'available':
					d_avialable[date].append(hour)
		return d_avialable

	@staticmethod
	def getall():
		db = pickledb.load(timedb, True, False)
		d_list = list(db.getall())
		all_timeslots = {}
		for dname in d_list:
			all_timeslots[dname] = TimeDB.get(dname)
		return all_timeslots

	@staticmethod
	def exist(dname):
		db = pickledb.load(timedb, True, False)
		return db.exists(dname)

	@staticmethod
	def check_dates(dname):
		db = pickledb.load(timedb, True, False)
		d_timeslots = db.get(dname)
		invalid_dates = []

		# delete invalid dates
		for date in d_timeslots:
			if not check_date(date):
				invalid_dates.append(date)
		if invalid_dates:
			for date in invalid_dates:
				del d_timeslots[date]

		# if the dates of the dentist is less than 3, add coming dates to his/her time slots
		if len(d_timeslots) < 3:
			coming_dates = get_coming_dates()
			for coming_date in coming_dates:
				if coming_date not in d_timeslots:
					d_timeslots[coming_date] = get_default_timeslots()
		db.set(dname, d_timeslots)
		db.dump()


class AppDB:
	@staticmethod
	def store(app_id, dname, date, hour):
		db = pickledb.load(appdb, True, False)
		db.set(app_id, {'dentist_name': dname, 'date': date, 'hour': hour})
		db.dump()

	@staticmethod
	def book(dname, date, hour):
		TimeDB.set(dname, date, hour, True)
		app_id = generate_appointment_id()
		AppDB.store(app_id, dname, date, hour)
		return app_id

	@staticmethod
	def cancel(dname, date, hour):
		TimeDB.set(dname, date, hour, False)
		db = pickledb.load(appdb, True, False)
		cancel_info = {}
		cancel_info['dentist_name'] = dname
		cancel_info['date'] = date
		cancel_info['hour'] = hour
		for app_id in list(db.getall()):
			if db.get(app_id) == cancel_info:
				db.rem(app_id)
				db.dump()
				break

	@staticmethod
	def cancel_by_id(app_id):
		db = pickledb.load(appdb, True, False)
		app_info = db.get(app_id)
		dname = app_info['dentist_name']
		date = app_info['date']
		hour = app_info['hour']
		TimeDB.set(dname, date, hour, False)
		db.rem(app_id)
		db.dump()

	@staticmethod
	def get(app_id):
		db = pickledb.load(appdb, True, False)
		return db.get(app_id)

	@staticmethod
	def exist(app_id):
		db = pickledb.load(appdb, True, False)
		return db.exists(app_id)
