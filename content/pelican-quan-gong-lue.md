Title:Pelican全攻略
Date:2015-06-15 22:30
Category:Tech
Tags:Python
Author:baijinping


Pelican是一套使用Python开发的开源静态网页生成工具。Pelican项目主页<http://www.getpelican.com/>。

------
[TOC]

## 安装Pelican
使用pip或者easy_install都可以。要下载最新的，还是到Pelican的github主页上下载吧：<https://github.com/getpelican>

安装过程中，还有一大堆的python库会依赖下载：

*	**feedgenerator**, to generate the Atom feeds
*	**jinja2**, for templating support
*	**pygments**, for syntax highlighting
*	**docutils**, for supporting reStructuredText as an input format
*	**pytz**, for timezone definitions
* 	**blinker**, an object-to-object and broadcast signaling system
*	**unidecode**, for ASCII transliterations of Unicode text
*	**six**, for Python 2 and 3 compatibility utilities
*	**MarkupSafe**, for a markup safe string implementation
*	**python-dateutil**, to read the date metadata

------

## 快速开始
安装完Pelican之后，可以在终端命令中找到`pelican-quickstart`。假设当前的目录是/home/mysite/，在该目录下运行`pelican-quickstart`命令，在经过n个询问的问题之后（也可以直接用默认的），Pelican就开始创建生成静态页面所需的文件了。
	生成后的目录树如下：
	![生成后的目录树]({attach}images/pelican-quickstart-filetree.png)

首先在content下创建一个测试文章（如下），保存为keyboard-review.md。
``` markdown
	Title: My First Review
	Date: 2010-12-03 10:20
	Category: Review

	Following is a review of my favorite mechanical keyboard.
```
回到/home/mysite目录，运行pelican content命令，Pelican就将页面生成到output目录下了。
进入output目录，启动python的内置http服务器：
``` shell
	python -m SimpleHTTPServer
```
访问<http://localhost:8000/>就可以看到生成好的网站了！
	![生成后的页面快照]({attach}images/pelican-quickstart-screenshot.png)
	
------
## Pelican配置简介

------
## 开始编写文章

------
## 文章中的链接

------
## 设置主题


------
## Pelican的缓存机制


------
## Pelican插件简介

------
## Pelican配置项详细说明

