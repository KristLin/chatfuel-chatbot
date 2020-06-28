# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from flask import jsonify, make_response

from . import Resource
from .. import schemas

from .database import TimeDB, AppDB


class AppointmentsAppointmentId(Resource):

	def get(self, appointment_id):
		app_id = appointment_id
		if not AppDB.exist(app_id):
			msg = {'messages': 'Appointment ID does not exist'}
			return make_response(jsonify(msg), 400)
		app_info = AppDB.get(app_id)
		msg = {'messages': app_info}
		return make_response(jsonify(msg), 200)

