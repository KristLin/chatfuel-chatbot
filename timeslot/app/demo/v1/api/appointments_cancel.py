# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from flask import jsonify, make_response

from . import Resource
from .. import schemas

from .database import TimeDB, AppDB


class AppointmentsCancel(Resource):

	def post(self):
		app_info = request.json
		dname = app_info['dentist_name'].lower()
		date = app_info['date']
		hour = app_info['hour']
		if not TimeDB.exist(dname):
			msg = {'messages': 'Dentist does not exist'}
			return make_response(jsonify(msg), 400)

		d_timeslots = TimeDB.get(dname)
		if date not in d_timeslots.keys():
			msg = {'messages': 'Invalid date'}
			return make_response(jsonify(msg), 400)

		if hour not in d_timeslots[date].keys():
			msg = {'messages': 'Invalid hour'}
			return make_response(jsonify(msg), 400)

		if d_timeslots[date][hour] == 'available':
			msg = {'messages': 'The timeslot is not reserved'}
			return make_response(jsonify(msg), 400)

		AppDB.cancel(dname, date, hour)
		msg = {'messages': 'The appointment is canceled'}
		return make_response(jsonify(msg), 200)
