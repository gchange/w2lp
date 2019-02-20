# -*- coding: utf-8 -*-

import hashlib
import tornado.web
import tornado.httpserver
from ..config import Config
from .message import Message
from http.server import HTTPStatus


class Handler(tornado.web.RequestHandler):
    def get(self):
        signature = self.get_argument("signature", None, True)
        timestamp = self.get_argument("timestamp", None, True)
        noce = self.get_argument("nonce", None, True)
        echostr = self.get_argument("echostr", None, True)

        list = [Config.SETTING["token"], timestamp, noce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        if hashcode != signature:
            self.send_error(HTTPStatus.UNAUTHORIZED)
            return

        self.write(echostr)

    def post(self, *args, **kwargs):
        msg = Message()
        msg.loads(self.request.body)
        self.write(msg.response())

