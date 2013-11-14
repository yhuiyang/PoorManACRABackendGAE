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

# GAE imports
from google.appengine.ext import ndb
# local imports


###########################################################################
# Report data
###########################################################################

###########################################################################
# Admin data
###########################################################################
class ApplicationConfiguration(ndb.Model):
    name = ndb.String(indexed=False, required=True)
    package = ndb.String(indexed=False, required=True)


class ApplicationManager(ndb.Model):
    app_cfg = ndb.LocalStructuredProperty(ApplicationConfiguration, repeated=True)

    @classmethod
    def getInstance(cls):
        return cls.get_or_insert('ApplicationManager', app_cfg=list())
