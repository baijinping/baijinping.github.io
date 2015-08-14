Title:Pelican全攻略
Date:2015-06-15 22:30
Category:Tech
Tags:Python
Author:baijinping
Summary:详细介绍了静态网页生成工具Pelican的使用方法，还有经过翻译的Setting项内容

Pelican是一套使用Python开发的开源静态网页生成工具。Pelican项目主页<http://www.getpelican.com/>。

------
[TOC]

## 一、安装Pelican
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

## 二、快速开始
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
## 三、Pelican配置简介
在前边生成的文件目录下，有两个配置文件pelicanconf.py和publishconf.py。其中主要是**pelicanconf.py**。可以这么认为，Pelican中可配置的值大部分已经有默认值，而用户可以在pelicanconf.py中对配置进行修改从而覆盖原来的值。

**推荐在pelicanconf.py中配置绝大部分的配置项，在需要发布时，将发布版本的配置放到publishconf.py中**（如生成发布版本时才需要SITEURL，DISQUS_SITENAME之类的配置）。publishconf.py的配置在生成发布版本时会覆盖掉pelicanconf.py中的相应配置。


------
## 四、开始编写文章
Pelican中使用‘**articles**’表示每一篇文章，每篇文章都会有自己的发布日期。‘articles’是易变的，经常会编辑的内容。
而‘**pages**’则表示不经常编辑改变的内容，如‘About’页，‘Contact’页。

**每种形式的文章都在某些特定的地方（通常是头部）提供文章的元数据**，如标题（title），发布日期（date），更新日期（modified），分类（category），标签（tags）等。

### Articles
Pelican中支持多种格式的源文章。包括reStructuredText格式（.rst后缀），Markdown格式等（.md,.markdown,.mkd,.mdown后缀都行），甚至包括Html格式（.html,.htm）。还有更多格式可以通过Pelican插件<http://github.com/getpelican/pelican-plugins>进行添加。

下面是几种常用格式的范例文章：
* reStructuredText:
``` rst
	My super title
	##############
	
	:date: 2010-10-03 10:20
	:modified: 2010-10-04 18:40
	:tags: thats, awesome
	:category: yeah
	:slug: my-super-post
	:authors: Alexis Metaireau, Conan Doyle
	:summary: Short version for index and feeds
```

* Markdown:
``` markdown
	Title: My super title
	Date: 2010-12-03 10:20
	Modified: 2010-12-05 19:30
	Category: Python
	Tags: pelican, publishing
	Slug: my-super-post
	Authors: Alexis Metaireau, Conan Doyle
	Summary: Short version for index and feeds

	This is the content of my super blog post.
```
* HTML:
``` html
<html>
    <head>
        <title>My super title</title>
        <meta name="tags" content="thats, awesome" />
        <meta name="date" content="2012-07-09 22:28" />
        <meta name="modified" content="2012-07-10 20:14" />
        <meta name="category" content="yeah" />
        <meta name="authors" content="Alexis Métaireau, Conan Doyle" />
        <meta name="summary" content="Short version for index and feeds" />
    </head>
    <body>
        This is the content of my super blog post.
    </body>
</html>
```

### Pages
如果在content目录下创建了pages目录，这个目录下的页面都是用来作为顶部导航栏的静态存在。一般用于About，Contact之类的页面。

### 文章元数据(File Metadata)追加内容

* 添加**Status:hidden**，**可以在目录中隐藏指向该文章页面的链接**。实测却不知为何，添加该元数据之后，生成该文章时居然报错了，当然最终目的页达到了——报错的页面都不会显示在目录中。

* 添加**Status:draft**，**可以使该文章不出现在任何标签页和分类页的列表中，算是用于页面的简单隐藏**。设置这个属性的html将会在单独的output/drafts目录下。
比如文章刚刚出了草稿，还不能发表，那就设置这个属性，单独将文章链接发给同事评价下吧。


------
## 五、文章中的链接
   

### filename链接-指向其他文章
如果需要创建指向某资源（其他页面，图片等）的链接，需要遵循语法：`{filename}path/to/file`

如果有如下的目录结构，而article1.rst和article2.md需要指向对方。
```
website/
├── content
│   ├── category/
│   │   └── article1.rst
│   ├── article2.md
│   └── pages
│       └── about.md
└── pelican.conf.py
```
在articles1.rst的正文中，指向articles2.md的链接格式应该是：
```
	`指向articles2的链接 <{filename}../articles2.md>`_
```
在articles2.md的正文中，指向articles1.rst的链接格式应该是：
```
	[指向articles1的链接]({filename}category/articles1.rst)
```
   
   

### filename链接-指向资源文件
如果要在文章中添加图片，可以创建content/images目录，图片直接放进去就可以了。默认配置下，images目录会自动拷贝到output中。但如果要放到其他的文件夹中，则需要在配置**STATIC_PATHS**中添加相应的目录。
	使用在markdown中创建链接的格式，将目标文件改为图片文件就可以了。**如果要让图片直接在文章中显示，则要在前面加上感叹号‘！’**。
```
	![显示图片的链接]({filename}images/hearthstone.jpg)
```
指向其他类型的文件都一样，点击后可以在浏览器中打开。
   
   
   
### attach链接-附件链接
除了使用{filename}作为前缀的链接以外，Pelican中还有另一种链接——**{attach}**。格式同{filename}，只是{}中的名字不同了。
**attach**，顾名思义就是附件的意思。**attach和filename最大的区别在于，使用attach指向的文件会在生成后被放到和源文章的相同目录下**，概念上就像源文章的附件一样。

**attach链接是不推荐使用的**。

关于attach要知道几点（链接文件表示被源文章attach的文件）：

1. 不管在content中链接文件和源文章的相对路径是怎样的，如果正常生成到了output中，那么链接文件至少是与源文章的html文件在同一目录下（如果在content时，链接文件就在源文章的目录内，如子目录，那么这个子目录会保留）；
2. 由于被attach后，静态文件的路径会发生改变，因此一个要求链接文件只能同时被一个源文章链接。如果一个静态文件被多个源文章链接（有大于等于一个attach链接），那么只有第一个attach链接会生效，其他的链接都不会被正常转义（怎么确定第一个是哪一个？都让你别这么用了）；
3. 能够正确使用attach的情境有两个：
	1. 确保对链接文件的attach链接都来自同一个文件；
	2. 所有发出attach链接的源文章都在同一个目录下。
   
   
   
### tag链接和category链接-指向标签页和分类页
最终的页面中会为每个tag和category生成单独的页，使用`{tag}path/to/file`和`{category}path/to/file`,可以**创建指向标签页和分类页的链接**。
   
   
   
### 向后兼容-|竖线|
为了保持向后兼容，Pelican暂时保留了使用竖线|作为链接符号的语法。目前这种语法已经不推荐使用。
之所以更换了语法，是为了避免竖线同Markdown插件和rst指令相冲突。**使用{花括号}的语法是目前推荐的**。


------
## 六、设置主题
从<https://github.com/getpelican/pelican-themes>可以获得几十个Pelican主题。
下载到本地之后，只要配置`THEME`为主题所在路径就可以了。

当然也可以自己创建主题， <http://docs.getpelican.com/en/3.5.0/themes.html>。


------
## 七、Pelican的缓存机制
**Pelican在生成时会使用缓存策略，以提高生成网页的速度**。这个缓存策略其实就是指，生成过程中会将源文章文件的一些数据放到缓存中，方便下一次生成过程判断源文章文件是否被更新了，生成过程只更新那些被更新了的articles和pages。

当Pelican获取到一个源文章文件（下文简称文章）时，将（‘处理该源文章’指的是开始生成该源文章文件对应的html页面）：

1. 如果`LOAD_CONTENT_CACHE`=True（默认），就尝试从上次生成缓存文件（保存路径配置在`CACHE_PATH`）中获取这个文章的hash值或更新时间值，并与当前的源文章文件的hash值或更新时间值进行比较；
2. 新旧文章的比较方法由`CHECK_MODIFIED_METHOD`配置。	->默认值为‘**mtime**’，即比较元数据更新时间
	1. 如果设置为hashlib模块中的某个hash函数（如‘md5’），则比较文件的hash值；
	2. 如果设置成其他值，或者无法获取到该文章在缓存中的任何数据，则处理该文章；
3. 如果比较后该文章被认为是未更新的，那么就从缓存中读取对应的数据进行生成。不处理该文章；
4. 如果比较后该文章被认为是有更新的，那么处理该文章。如果`CACHE_CONTENT`=True，则将其添加到缓存文件中。


几点补充：

1. `CONTENT_CACHING_LAYER`可以设置被缓存的数据内容。默认值为’**reader**’，表示整个源文章文件和元数据。可选值为’**generator**’，缓存的是经过处理后的数据（下一次处理起来会更快）。但是不推荐配置为’generator’，虽然速度会快一点，但可能会与一些插件或`WITH_FUTURE_DATES`的设置发生冲突，产生一些奇怪的问题；
2. `CHECK_MODIFIED_METHOD`默认比较’**mtime**’，这种方式的速度比使用hash进行比较更快。但要考虑到元数据更新时间值在有些时候会丢失；
3. 缓存文件通过Python的pickles进行保存，因此在更换Python版本后，需要移除缓存文件重新进行生成（pickles格式在不同版本的Python中可能不同）。另外，如果`GZIP_CACHE`更改的话，也要移除缓存文件重新进行生成；
4. 尽管在生成过程中缓存了源文章，但是生成目录下的html文件始终会更新（不管源文章是否有更新）。提交时可以使用`—checksum`表示检查校验和。



------
## 八、Pelican插件简介
Pelican从3.0开始支持插件。使用插件能够在不修改Pelican的情况下增加更多功能。
Pelican的所有插件都在这里：<https://github.com/getpelican/pelican-plugins>，该页面下方还有各个插件的说明。

使用插件有两种形式：

1. 一是在当前python环境中可以直接import得到的，这种情况下使用`PLUGINS`参数进行配置。
	这种配置也有两种形式（一起用也是可以的）：
	1-> PLUGINS = [‘package.myplugin’,]
	2-> from package import myplugin 
	2->PLUGINS = [myplugin,]

2. 二是当插件代码无法直接import时，直接指定插件的路径，这种情况下使用`PLUGIN_PATHS`参数进行配置。
	-> PLUGIN_PATHS = [‘plugins’, ‘/srv/pelican/plugins’]
	-> PLUGINS = [‘asserts’, ‘liquid_tags’, ‘sitemap’]
	在查找时就会在/srv/pelican/plugins/目录下查找。我想其机制应该时将那个路径添加到sys.path里边，然后尝试import。


在生成页面的时候，pelican主程序会与各个插件进行通信，这里<http://docs.getpelican.com/en/3.5.0/plugins.html#list-of-signals>定义了通信的数据格式。如果需要编写插件，可以深入看看，这里不展开。

------
## 九、Pelican配置项详细说明

### Pelican基础配置项列表
官方文档见<http://docs.getpelican.com/en/3.5.0/settings.html>

| 配置项名(=默认值)			 | 中文说明	 |
| :------------------------------------------------: | :------------------: |
| AUTHOR | 作者名字 |
| DATE_FORMATS = {} | 为不同语言环境设置不同的日期格式 |
| USE_FOLDER_AS_CATEGORY = True | 是否使用文章所在文件夹名称作为文章的category属性值 |
| DEFAULT_CATEGORY = 'misc' | 默认category值 |
| DEFAULT_DATE_FORMAT = '%a %d %B %Y' | 默认日期时间格式 |
| DISPLAY_PAGES_ON_MENU = True | 是否将pages目录下的文章标题显示在顶部菜单栏 |
| DISPLAY_CATEGORIES_ON_MENU = True | 是否将文章中的分类显示在顶部菜单栏 |
| DEFAULT_DATE = None | 默认日期值 |
| DEFAULT_METADATA = () | 为所有页面设置默认元数据值 |
| DOCUTILS_SETTINGS = {} | （针对reStructuredText格式）docutils的额外输出配置 |
| FILENAME_METADATA ='\(?P&lt;date>\\d\{4\}-\\d\{2\}-\\d\{2\}\).*' | 这是一个正则表达式，用于从文章的文件名中找到一些匹配的元数据作为该文章的元数据 |
| PATH_METADATA = '' | 类似FILENAME_METADATA，但PATH_METADATA是从文章保存的路径进行正则查找的 |
| EXTRA_PATH_METADATA = {} | 为一些特定的路径下的文章设定默认元数据 |
| DELETE_OUTPUT_DIRECTORY = False | 重新生成之前，是否先删除output下的所有文件 |
| OUTPUT_RETENTION = () | 当重新生成前要删除output时，设定一些文件保留下来，不被删除掉 |
| JINJA_EXTENSIONS = [] | 设定Jinja的扩展 |
| JINJA_FILTERS = {} | 使用到的Jinja过滤器，不太明白 |
| LOCALE | 设置区域 |
| LOG_FILTER = [] | 设置生成时的日志过滤 |
| READERS = {} | 用来增加/删除某些格式文件的生成器 |
| IGNORE_FILES = ['.#*'] | 生成时，不作处理的文件名规则 |
| MD_EXTENSIONS =\['codehilite\(css_class=highlight\)','extra'\] | 添加Markdown扩展 |
| OUTPUT_PATH = 'output/' | 设置生成的网页文件存放路径 |
| PATH | 设置content目录的路径 |
| PAGE_PATHS = ['pages'] | 设定某些目录下的文章被视为pages同等存在 |
| PAGE_EXCLUDES = [] | 设定哪些目录需要在查找pages同等存在时被排除（不需要指定ARTICLE_PATHS） |
| ARTICLE_PATHS = [''] | 设定某些目录下的文章被视为articles同等存在 |
| ARTICLE_EXCLUDES = [] | 设定哪些目录需要在查找articles同等存在时被排除（不需要指定PAGE_PATHS） |
| OUTPUT_SOURCES = False | 生成时网页时是否将源文章也一同拷贝到OUTPUT_PATH |
| OUTPUT_SOURCES_EXTENSION = '.text' | 没懂 |
| RELATIVE_URLS = False | 是否将url设为基于本地文件的url。若设为True，则本地可以测试，否则本地测试不了 |
| PLUGINS = [] | 需要接入的插件列表。可以有两种形式：1是完整包路径，2是直接import进来之后，放入import进来的插件模块 |
| PLUGIN_PATHS = [] | 当插件无法直接import进来时，在这里设定查找插件的路径 |
| SITENAME = 'A Pelican Blog' | 网站名称 |
| SITEURL | 网站实际域名，e.g.http://mydomain.com |
| TEMPLATE_PAGES = None | 用来生成顶级的文章（category在菜单栏上），并且文章的内容完全由源html文件渲染。这是字典类型，key表示content目录下源html文件的路径，value表示output下生成的对应网页的路径 |
| STATIC_PATHS = ['images'] | 指定content下属于静态资源的目录。在STATIC_PATHS中包含了的目录才会被拷贝到output中去。在这些目录中，复合格式的源文章依然能够被解析，但源文章在静态目录拷贝过程中将被排除。因此不需要担心在output中的images看到源文件的出现~我测试时，发现images中的文章被直接放到output/下了。但是，如果设定了STATIC_EXCLUDE_SOURCES为True，那么源文章也会直接拷贝到output/images下 |
| STATIC_EXCLUDES = [] | 设定哪些路径在查找静态目录时要被排除 |
| STATIC_EXCLUDE_SOURCES = True | 设定静态文件目录中的源文章是否一起拷贝到output |
| TIMEZONE | 设置时区 |
| TYPOGRIFY = False | 如果设置为True，将会使用typogrify库对HTML进一步的修饰 |
| TYPOGRIFY_IGNORE_TAGS = [] | 设置typogrify库在修饰HTML代码时，不进行修饰的标签 |
| DIRECT_TEMPLATES =('index', 'categories', 'authors', 'archives') | 用于直接渲染内容的模板列表。一般来说，这些模板用于生成索引页，包括主页，标签页，分类页，归档页等 |
| PAGINATED_DIRECT_TEMPLATES = ('index',) | 需要使用标签页的模板 |
| SUMMARY_MAX_LENGTH = 50 | 文章简介的默认长度。当文章没有设定Summary时使用。如果设置None则表示原文作为简介 |
| EXTRA_TEMPLATES_PATHS = [] | 没懂 |
| WITH_FUTURE_DATES = True | 对于元数据发布时间在未来的文章，是否设置特殊状态 |
| INTRASITE_LINK_REGEX = '\[\{¦\]\(?P&lt;what>.*?\)\[¦\}\]' | 设置内部链接的格式 |
| PYGMENTS_RST_OPTIONS = [] | 针对rst格式，添加对Pygments的设置 |
| SLUGIFY_SOURCE = 'title' | 设置源文章自动生成slug的方式（默认使用title元数据进行生成） |
| CACHE_CONTENT = True | 是否使用缓存 |
| CONTENT_CACHING_LAYER = 'reader' | 设置缓存保存的文章数据内容 |
| CACHE_PATH = 'cache' | 设置缓存文件保存的路径 |
| GZIP_CACHE = True | 是否使用gzip对缓存文件进行压缩 |
| CHECK_MODIFIED_METHOD = 'mtime' | 设置检查源文章是否有更新的策略 |
| LOAD_CONTENT_CACHE = True | 是否从缓存中获取文章数据进行比较生成 |
| AUTORELOAD_IGNORE_CACHE = False | 是否自动忽略缓存（等同于生成时使用—ignore-cache参数），缓存会被直接覆盖 |
| WRITE_SELECTED = [] | 设置在生成时被重新生成的output路径。默认是整个output都重新生成一次。当某些情况下只需要微调一两个页面时，生成的速度会提高，调试的效率也提高了 |


