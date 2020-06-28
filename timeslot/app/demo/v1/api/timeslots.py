# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from flask import jsonify, make_response

from . import Resource
from .. import schemas

from .database import TimeDB, AppDB


class Timeslots(Resource):

	def get(self):
		timeslots = TimeDB.getall()
		msg = {'messages': timeslots}
		return make_response(jsonify(msg), 200)

	def post(self):
		print(request.json)
		dname = request.json['dentist_name'].lower()
		TimeDB.store(dname)
		msg = {'messages': 'Timeslots created'}
		return make_response(jsonify(msg), 200)
