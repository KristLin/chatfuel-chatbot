# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from flask import jsonify, make_response

from . import Resource
from .. import schemas

from .database import DB


class DentistsDentistName(Resource):

	def get(self, dentist_name):
		dname = dentist_name.lower()
		if not DB.exist(dname):
			msg = {'messages': 'The dentist does not exist'}
			return make_response(jsonify(msg), 400)
		dinfo = {dname: DB.get(dname)}
		msg = {'messages': dinfo}
		return make_response(jsonify(msg), 200)
