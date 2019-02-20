# -*- coding: utf-8 -*-


class Config(object):
    SETTING = {}
    __slots__ = []

    @classmethod
    def __getattr__(cls, item: str):
        return cls.SETTING.get(item)

    @classmethod
    def __setattr__(cls, key: str, value):
        cls.SETTING[key] = value
