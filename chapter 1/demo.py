#!/usr/bin/env python

from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

print("\n获取所有的连接\n")
links = soup.find_all('a')

for link in links:
    print(link.name, link.get_text(), link['href'])

print("\n获取laxie的连接")
link_node = soup.find('a', href='http://example.com/lacie')
print(link.name, link.get_text(), link['href'])

print("正则匹配\n")
link_node = soup.find('a', href=re.compile(r"ill"))
print(link.name, link.get_text(), link['href'])

print("获取p段落名称\n")
p_node = soup.find('p', class_="title")
print(p_node.name, p_node.get_text())


