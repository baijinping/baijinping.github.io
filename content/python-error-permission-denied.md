Title:Python(Errno13)PYTHON_EGG_CACHE设置 
Date:2014-11-16 11:00
Category:Tech
Tags:Python
Slug:python-error-permission-denied

#Error Information
这次由我重新设计网站目录结构,并重新安装时,出现了如下异常:

```Can't extract file(s) to egg cache The following error occurred while trying to extract file(s) to the Python egg cache: [Errno 13] Permission denied: '/usr/share/httpd/.python-eggs' The Python egg cache directory is currently set to: /usr/share/httpd/.python-eggs Perhaps your account does not have write access to this directory? You can change the cache directory by setting the PYTHON_EGG_CACHE environment variable to point to an accessible directory.
```

---
#Environment
* CentOS 7
* Python 2.7.5
* Apache 2.4.6 + module_wsgi
* web.py

---
#Analyse
如果某个Python库在安装后没有解压,以压缩包的形式存在于site-package/等Python库目录下,那么在这些库被引用时,将被解压到某个临时目录，python则直接引用这个临时目录下的库文件。
那出现权限异常的原因就出来了，python没用足够权限访问（w+r）存放临时文件的目录。
根据我自身的情况，是其实这个目录并不存在。

#Solution
在/usr/share/httpd/目录下创建.python-eggs目录,将该目录的权限设为777.重新访问即可。

#Reference

* [http://blog.csdn.net/imzkz/article/details/5568585](http://blog.csdn.net/imzkz/article/details/5568585)
* [http://code.google.com/p/modwsgi/wiki/ApplicationIssues#Access_Rights_Of_Apache_User](http://code.google.com/p/modwsgi/wiki/ApplicationIssues#Access_Rights_Of_Apache_User)


