Title:在阿里云上运行docker服务
Date:2015-07-19 10:57
Category:Tech
Tags:docker
Author:baijinping
Summary:解决在阿里云中运行docker服务的FATA[0000]错误


在**阿里云**上部署了一台云主机(**centos 7**，想尝试下docker技术，但第一次运行却不成功，报下面这个错误。
运行命令: systemctl start docker
结果提示错误：**FATA[0000] Get http:///var/run/docker.sock/v1.18/containers/json?all=1: dial unix /var/run/docker.sock: no such file or directory. Are you trying to connect to a TLS-enabled daemon without TLS? **


### 资料
------

在网上找到MicroTeam的一篇阿里云上Debian运行docker时，遇到相同错误的解决方法<http://www.cnblogs.com/MicroTeam/p/see-docker-run-in-debian-with-aliyun-ecs.html>。参考这篇帖子，通过更改网络配置解决了这个问题。


### 解决方案
------

解决方法如下：
在/etc/sysconfig/network-scripts中将route-eth0中的路由规则改变：

1. 将172.16.0.0/12 via 10.169.231.247 dev eth0这一行加上注释（前边加'#'）
2. 重启network服务：systemctl restart network
3. 启动docker服务：systemctl start docker





