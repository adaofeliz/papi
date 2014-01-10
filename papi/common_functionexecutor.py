# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from config import config

import concurrent.futures

class FunctionExecutor:

	def __init__(self):
		self.function_Executor = concurrent.futures.ThreadPoolExecutor(max_workers=50)

	def execute(self, functions):

		return_dict = {}
		process_array = []

		for function in functions:
			process_array.append(self.function_Executor.submit(function['target'], function['args']))

		for future in concurrent.futures.as_completed(process_array):

			try:
				return_dict.update(future.result())
			except Exception as exc:
				print('generated an exception: %s' % (exc))

		return return_dict

# Singleton
executor = FunctionExecutor()