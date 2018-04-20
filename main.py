# -*- coding: utf-8 -*-
# filename: main.py
import web

urls = (
  '/.*', 'Handle',
)

class Handle(object):
  def GET(self):
    return "hello, this is a test"

app = web.application(urls, globals(),autoreload=False)
application = app.wsgifunc()
