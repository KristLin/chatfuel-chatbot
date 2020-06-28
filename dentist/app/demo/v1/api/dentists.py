# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from flask import jsonify, make_response

from . import Resource
from .. import schemas

from .database import DB
import requests


class Dentists(Resource):

	def get(self):
		dlist = DB.getall()
		msg = {'messages': dlist}
		return make_response(jsonify(msg), 200)

	def post(self):
		dinfo = request.json
		dname = dinfo['dentist_name'].lower()
		if DB.exist(dname):
			msg = {'messages': 'Dentist already exists'}
			return make_response(jsonify(msg), 400)

		url = "http://timeslot:3000/v1/timeslots"
		data = {'dentist_name': dname}
		response = requests.post(url, json=data)
		# update the timeslot database first
		if response.status_code == 200:
			dloc = dinfo['location']
			dspec = dinfo['specialization']
			DB.store(dname, dloc, dspec)
			msg = {'messages': 'Dentist is added'}
			return make_response(jsonify(msg), 200)
		else:
			msg = {'messages': 'Failed to update the database'}
			return make_response(jsonify(msg), 400)
