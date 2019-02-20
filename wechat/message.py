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

    __slots__ = ["data"]

    def __init__(self):
        self.data = {}

    def loads(self, text: str):
        root = ElementTree.fromstring(text)
        self.data = {child.tag: child.text for child in root}

    def dump(self, data):
        root = ElementTree.Element("xml")
        for key, val in data.items():
            child = ElementTree.SubElement(root, key)
            child.text = val
        return ElementTree.dump(root)

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
            return "success"
        return self.dump(self.data)
