import pickledb

dentistdb = 'dentist.db'


class DB:
	@staticmethod
	def store(dname, dloc, dspec):
		db = pickledb.load(dentistdb, True, False)
		db.set(dname, {'location': dloc, 'specialization': dspec})

	@staticmethod
	def get(dname):
		db = pickledb.load(dentistdb, True, False)
		return db.get(dname)

	@staticmethod
	def getall():
		db = pickledb.load(dentistdb, True, False)
		return list(db.getall())

	@staticmethod
	def exist(dname):
		db = pickledb.load(dentistdb, True, False)
		return db.exists(dname)