# -*- coding: utf-8 -*-

import hashlib
import tornado.web
import tornado.httpserver
from ..config import Config
from .message import Message
from http.server import HTTPStatus


class Handler(tornado.web.RequestHandler):
    def __init__(self, application: tornado.web.Application, request: tornado.httpserver.HTTPRequest, **kwargs):
        super(Handler, self).__init__(application, request, **kwargs)
        self.echostr = ""

    def get(self):
        signature = self.get_argument("signature", None, True)
        timestamp = self.get_argument("timestamp", None, True)
        noce = self.get_argument("nonce", None, True)
        self.echostr = self.get_argument("echostr", None, True)

        list = [Config["token"], timestamp, noce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        if hashcode != signature:
            self.send_error(HTTPStatus.UNAUTHORIZED)

    def post(self, *args, **kwargs):
        msg = Message()
        msg.loads(self.request.body)
        self.write(msg.response())

