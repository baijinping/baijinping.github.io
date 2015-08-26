Title:firewalld重新加载配置
Date:2015-08-21 20:45
Category:Tech
Tags:Linux
Author:baijinping
Summary:firewalld服务重新加载配置的两种方式比较

配置文件路径：/etc/firewalld/

firewall-cmd --reload
重新加载配置，但不影响已经创建的连接的服务

firewall-cmd --complete-reload
重新加载配置，同时关闭所有已经创建的连接



