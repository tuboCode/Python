#!/usr/bin/env python

from urllib import request
from urllib import request
from urllib import parse

# req = request.Request("https://www.thsrc.com.tw/tw/TimeTable/SearchResult")
req = request.Request("http://www.yangtzeu.edu.cn/")

req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3080.5 Safari/537.36")

postData = parse.urlencode([
    ("StartStation", "977abb69-413a-4ccf-a109-0272c24fd490"),
    ("EndStation", "9c5ac6ca-ec89-48f8-aab0-41b738cb1814"),
    ("SearchDate", "2017/07/17"),
    ("SearchTime", "23:00"),
    ("SearchWay", "DepartureInMandarin"),
])

resp = request.urlopen(req)

print(resp.read().decode("utf-8"))
