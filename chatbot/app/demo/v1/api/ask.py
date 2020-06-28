# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from flask import jsonify, make_response

from . import Resource
from .. import schemas
import json
from rivescript import RiveScript


class Ask(Resource):

	def post(self):
		# print(g.args)
		# msg = g.args['message']
		msg = request.form["message"]

		bot = RiveScript()
		bot.load_directory("./v1/api/brain")
		bot.sort_replies()

		reply = bot.reply("localuser", msg)
		print()
		print('You>', msg)
		print('Bot>', reply)
		error_msg = ["[ERR: Error when executing Python object]", "[ERR: No Reply Matched]", "[ERR: Object Not Found]"]
		if reply in error_msg:
			reply = "sorry, I don't understand you..."

		answer = {'messages': [{"text": reply}]}
		return make_response(jsonify(answer), 200)
