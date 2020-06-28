import requests

port = 3000
addr = 'timeslot'


def check_format(date, hour):
	# handle the date with no symbols (data from RiveScript)
	if '/' not in date:
		date = date[:2] + '/' + date[2:4] + '/' + date[4:]
	if '-' not in hour:
		if hour[0] == '9':
			hour = hour[0] + '-' + hour[1:]
		else:
			hour = hour[:2] + '-' + hour[2:]
	return date, hour


def get_recommand_time(dentist_name):
	url = "http://{}:{}/v1/timeslots/{}/available".format(addr, port, dentist_name)
	response = requests.get(url)
	dentist_available_timeslots = response.json()['messages']
	if not dentist_available_timeslots:
		return False, 0, 0
	else:
		date_num = len(dentist_available_timeslots)
		from random import randrange
		date_index = randrange(date_num)
		date = list(dentist_available_timeslots.keys())[date_index]
		timeslot_num = len(dentist_available_timeslots[date])
		timeslot_index = randrange(timeslot_num)
		timeslot = dentist_available_timeslots[date][timeslot_index]
		return True, date, timeslot


def get_dentist_available_timeslots(dentist_name):
	dentist_name = dentist_name.lower()
	url = "http://{}:{}/v1/timeslots/{}/available".format(addr, port, dentist_name)
	response = requests.get(url)
	if response.status_code == 200:
		dentist_available_timeslots = response.json()['messages']
		if dentist_available_timeslots:
			reply = 'His/Her available times are: \n'
			for date in dentist_available_timeslots:
				reply += date + ': \n'
				for hour in dentist_available_timeslots[date]:
					reply += hour + ', '
				reply = reply.strip(', ')
				reply += '\n'
			reply += '\n'
			reply += 'Now you can book a reservation, just tell me the dentist and his/her timeslot :)'
			return reply
		else:
			reply = 'Oops! The dentist has no available time now.'
			return reply
	else:
		reply = 'Oops! ' + response.json()['messages']
		reply += '.'
		return reply


def reserve_timeslot(dentist_name, date, hour):
	dentist_name = dentist_name.lower()
	date, hour = check_format(date, hour)
	url = "http://{}:{}/v1/appointments/book".format(addr, port)
	data = {'dentist_name': dentist_name, 'date': date, 'hour': hour}
	response = requests.post(url, json=data)

	if response.status_code == 200:
		appointment_id = response.json()['messages']['app_id']
		reply = 'Great! I booked an appointment for you: \n'
		start_hour, end_hour = hour.split('-')
		reply += 'Dr. {} on {} from {} to {}, '.format(dentist_name, date, start_hour, end_hour)
		reply += 'your appointment id is {}'.format(appointment_id)
		reply += '.'
		return reply
	else:
		msg = response.json()['messages']
		if msg in ['The timeslot is not available', 'Invalid date', 'Invalid hour']:
			flag, recommend_date, recommand_timeslot = get_recommand_time(dentist_name)
			if flag:
				reply = 'Oops! {}. '.format(msg)
				reply += 'Would you like to book {} {}?'.format(recommend_date, recommand_timeslot)
				return reply
			else:
				reply = 'Oops! The dentist has no available time...'
				return reply
		reply = 'Oops! ' + msg
		reply += '.'
		return reply


def cancel_timeslot(dentist_name, date, hour):
	dentist_name = dentist_name.lower()
	date, hour = check_format(date, hour)
	start_hour, end_hour = hour.split('-')
	appointment_info = 'Appointment Info: Dr. {} on {} from {} to {}.'.format(dentist_name, date, start_hour, end_hour)
	url = "http://{}:{}/v1/appointments/cancel".format(addr, port)
	data = {'dentist_name': dentist_name, 'date': date, 'hour': hour}
	response = requests.post(url, json=data)
	if response.status_code == 200:
		reply = response.json()['messages']
		reply += '.\n'
		reply += appointment_info
		return reply
	else:
		reply = 'Oops! ' + response.json()['messages']
		reply += '.'
		return reply


def cancel_timeslot_by_id(appointment_id):
	appointment_info = check_appointment(appointment_id)
	url = "http://{}:{}/v1/appointments/{}/cancel".format(addr, port, appointment_id)
	response = requests.get(url)
	if response.status_code == 200:
		reply = response.json()['messages']
		reply += '.\n'
		reply += appointment_info
		return reply
	else:
		reply = 'Oops! ' + response.json()['messages']
		reply += '.'
		return reply


def check_appointment(appointment_id):
	url = "http://{}:{}/v1/appointments/{}".format(addr, port, appointment_id)
	response = requests.get(url)

	if response.status_code == 200:
		appointment_info = response.json()['messages']
		dentist_name = appointment_info['dentist_name']
		date = appointment_info['date']
		hour = appointment_info['hour']
		start_hour, end_hour = hour.split('-')
		reply = 'Appointment Info: Dr. {} on {} from {} to {}.'.format(dentist_name, date, start_hour, end_hour)
		return reply
	else:
		reply = 'Oops! ' + response.json()['messages']
		reply += '.'
		return reply
