# -*- coding: utf-8 -*-

import hashlib
import tornado.web
import tornado.httpserver
import logging
from ..config import Config
from .message import Message
from http.server import HTTPStatus


class Handler(tornado.web.RequestHandler):
    def get(self):
        signature = self.get_argument("signature", None, True)
        timestamp = self.get_argument("timestamp", None, True)
        noce = self.get_argument("nonce", None, True)
        echostr = self.get_argument("echostr", None, True)

        args = [Config.SETTING["token"], timestamp, noce]
        args.sort()
        sha1 = hashlib.sha1("".join(args).encode("utf8"))
        hashcode = sha1.hexdigest()
        if hashcode != signature:
            self.send_error(HTTPStatus.UNAUTHORIZED)
            logging.error("signature: %s != %s", hashcode, signature)
            return

        self.write(echostr)

    def post(self, *args, **kwargs):
        msg = Message()
        msg.loads(self.request.body)
        self.write(msg.response().encode("utf8"))

