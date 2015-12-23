# -*- coding: utf-8 -*-
'''
Created on Mar 14, 2012

@author: moloch

    Copyright 2012 Root the Box

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
'''


from tornado.web import UIModule
from tornado.options import options


class Recaptcha(UIModule):

    def render(self, *args, **kwargs):
        if options.use_recaptcha:
            return self.render_string('recaptcha/captcha.html')
        else:
            return self.render_string('recaptcha/disabled.html')
