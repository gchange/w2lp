# -*- coding: utf-8 -*-

import argparse
import json

from .config import Config
from .wechat.authorize import AuthorizeHandler

import tornado.ioloop
import tornado.web


def make_app():
    return tornado.web.Application([
        (r"/wechat", AuthorizeHandler),
    ])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="config file", type=str, default="config.json")
    args = parser.parse_args()

    with open(args.config, "rb") as f:
        data = json.load(f)
    for k, v in data:
        Config[k] = v

    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
