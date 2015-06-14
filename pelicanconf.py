#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'baijinping'
SITENAME = u"baijinping's world"
SITEURL = 'www.baijinping.com'

TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = u'cn'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

THEME = 'F:\pelican-themes-master\pelican-bootstrap3'
#THEME = 'F:\pelican-themes-master\lightweight'
# THEME = 'F:\pelican-themes-master\\notmyidea-cms'


PATH = 'content'
OUTPUT_PATH = ''
# 设置content中的静态资源目录，只有在这里指定了，才会被拷贝到output中
# 如果没有这个遍历，则默认只有images目录会自动拷贝到output
STATIC_PATHS = ['images', 'pdfs', 'favicon.ico']

ARCHIVES_URL = 'archives.html'
ARTICLE_URL = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Plugins
GITHUB_URL = 'https://github.com/baijinping'
GOOGLE_ANALYTICS = 'UA-56594205-1'
DISQUS_SITENAME = 'wwwbaijinpingcom'

# Blogroll
LINKS = (('老博客', 'http://baikkp.blog.51cto.com/'),
	('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/baijinping'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# 生成时是否使用先前缓存的数据
LOAD_CONTENT_CACHE = False

# 是否将content/pages/下的文章直接放到顶部导航栏
DISPLAY_PAGES_ON_MENU = True

# 如果文章没有提供Summary属性，则设置文章开头一定长度的文本作为摘要
SUMMARY_MAX_LENGTH = None

# 是否将文章的分类放到菜单栏
DISPLAY_CATEGORIES_ON_MENU = True

# 是否使用typogrify库进一步修饰html标签
TYPOGRIFY = True

# 生成之前是否先清空output目录
# DELETE_OUTPUT_DIRECTORY = True


