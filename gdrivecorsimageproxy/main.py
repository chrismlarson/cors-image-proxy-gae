#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
import webapp2
from google.appengine.api import urlfetch

class MainHandler(webapp2.RequestHandler):
    def get(self):
        imageId = self.request.get('imageId')
        url = 'http://drive.google.com/uc?export=view&id=' + imageId

        response = urlfetch.fetch(url=url,
                                  method=urlfetch.GET)

        #contentTypeHeader = self.response.headers.get('Content-Type')

        self.response.headers.add_header("Access-Control-Allow-Origin", '*')
        self.response.headers['Content-Type'] = 'image/png'
        self.response.status = response.status_code
        self.response.write(response.content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
