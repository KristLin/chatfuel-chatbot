# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from flask import jsonify, make_response

from . import Resource
from .. import schemas

from .database import TimeDB, AppDB


class TimeslotsDentistNameAvailable(Resource):

	def get(self, dentist_name):
		dname = dentist_name.lower()
		if not TimeDB.exist(dname):
			msg = {'messages': 'Dentist does not exist'}
			return make_response(jsonify(msg), 400)
		d_available_timeslots = TimeDB.get_available(dname)
		msg = {'messages': d_available_timeslots}
		return make_response(jsonify(msg), 200)
