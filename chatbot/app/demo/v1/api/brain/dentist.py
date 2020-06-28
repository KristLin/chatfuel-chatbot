import requests

port = 4000
addr = 'dentist'


def get_all_dentists():
	url = "http://{}:{}/v1/dentists".format(addr, port)
	response = requests.get(url)
	if response.status_code == 200:
		dentists = response.json()['messages']
		if dentists:
			if len(dentists) > 1:
				reply = 'Working dentists are '
			else:
				reply = 'The working dentist is '
			for dentist in dentists[:-1]:
				reply += dentist + ', '
			reply = reply.strip(', ')
			reply += ' and ' + dentists[-1] + '. Which dentist do you prefer?'
			return reply
		else:
			reply = 'Sorry, there are no dentists are working right now...'
			return reply
	else:
		reply = 'Oops! ' + response.json()['messages']
		reply += '.'
		return reply


def get_dentist_info(dentist_name):
	dentist_name = dentist_name.lower()
	url = "http://{}:{}/v1/dentists/{}".format(addr, port, dentist_name)
	response = requests.get(url)
	if response.status_code == 200:
		dentist_info = response.json()['messages']
		reply = dentist_name + ' specializes in ' + dentist_info[dentist_name]['specialization'] \
				+ ", working in " + dentist_info[dentist_name]['location']
		reply += '.'
		return reply
	else:
		reply = 'Oops! ' + response.json()['messages']
		reply += '.'
		return reply
