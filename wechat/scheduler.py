# -*- coding: utf-8 -*-

import aiohttp
import logging
from http.server import HTTPStatus
from ..config import Config


class Scheduler(object):
    @staticmethod
    async def refresh_token():
        appid = Config.SETTING["appid"]
        secret = Config.SETTING["secret"]
        grant_type = "client_credential"

        url = Config.SETTING["wechat"] + "/cig-bin/token"
        resp = await aiohttp.request("GET", url, params=dict(grant_type=grant_type, appid=appid, secret=secret))
        if resp.status != HTTPStatus.OK:
            logging.error("status: %d reason: %s", resp.status, resp.reason)
            return

        data = await resp.json()
        if data.get("errcode") is not None:
            logging.error("code: %d msg", data.get("errcode", 0), data.get("msg", ""))
            return

        access_token = data.get("access_token")
        expire = data.get("expires_in")
        if not access_token or not expire:
            logging.error("token: %s expire: %s", access_token, expire)
            return
