# -*- coding: utf-8 -*-

import argparse
import json
import tornado.ioloop
import tornado.web
from .config import Config
from .wechat.handler import Handler


def make_app():
    return tornado.web.Application([
        (r"/wechat", Handler),
    ])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="config file", type=str, default="config.json")
    parser.add_argument("--port", help="listen port", type=int, default=80)
    args = parser.parse_args()

    with open(args.config, "r") as f:
        data = json.load(f)
    Config.SETTING.update(data)

    app = make_app()
    app.listen(args.port)
    tornado.ioloop.IOLoop.current().start()
