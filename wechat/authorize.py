# -*- coding: utf-8 -*-

from .handler import Handler


class AuthorizeHandler(Handler):
    def get(self, *args, **kwargs):
        self.write(self.echostr)
