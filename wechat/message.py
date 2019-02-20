# -*- coding: utf-8 -*-

from xml.etree import ElementTree


class Message(object):
    MSG_TYPE_TEXT = "text"
    MSG_TYPE_IMAGE = "image"
    MSG_TYPE_VOICE = "voice"
    MSG_TYPE_VIDEO = "video"
    MSG_TYPE_SHORT_VIDEO = "shortvideo"
    MSG_TYPE_LOCATION = "location"
    MSG_TYPE_LINK = "link"

    INT_TYPE_DATA = ("CreateTime",)

    __slots__ = ["data"]

    def __init__(self):
        self.data = {}

    def parse_data(self, key, val):
        return val

    def pack_data(self, key, val):
        if key in self.INT_TYPE_DATA:
            return str(val)
        return "![CDATA[" + val + "]]"

    def loads(self, text: str):
        root = ElementTree.fromstring(text)
        self.data = {child.tag: self.parse_data(child.tag, child.text) for child in root}

    def dump(self, data):
        root = ElementTree.Element("xml")
        for key, val in data.items():
            child = ElementTree.SubElement(root, key)
            child.text = self.pack_data(key, val)
        return ElementTree.tostring(root)

    def response(self):
        msg_type = self.data["MsgType"]
        if msg_type == self.MSG_TYPE_TEXT:
            pass
        elif msg_type == self.MSG_TYPE_IMAGE:
            pass
        elif msg_type == self.MSG_TYPE_VOICE:
            pass
        elif msg_type == self.MSG_TYPE_VIDEO:
            pass
        elif msg_type == self.MSG_TYPE_SHORT_VIDEO:
            pass
        elif msg_type == self.MSG_TYPE_LOCATION:
            pass
        elif msg_type == self.MSG_TYPE_LINK:
            pass
        else:
            return b"success"
        data = {}
        data.update(self.data)
        data["ToUserName"], data["FromUserName"] = data["FromUserName"], data["ToUserName"]
        return self.dump(self.data)
