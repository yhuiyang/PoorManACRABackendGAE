#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2013, YH Yang <yhuiyang@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# python imports
import logging


# GAE imports
import webapp2
from webapp2_extras.routes import RedirectRoute

# local imports


class PostHandler(webapp2.RequestHandler):

	def post(self):

		logging.info('post handler invoked')
		for k, v in self.request.POST.items():
			logging.debug('%s: %s' % (k, v))


class PutHandler(webapp2.RequestHandler):

	def put(self, report_id):

		logging.info('put handler invoked: %s' % report_id)


routes = [
    RedirectRoute(r'/', handler=PostHandler, name='post-report-collector', strict_slash=True),
    RedirectRoute(r'/<report_id:[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}>',
                  handler=PutHandler, name='put-report-collector', strict_slash=True),
]
