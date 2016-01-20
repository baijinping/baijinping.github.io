Title:Redis启动警告及处理方法
Date:2015-08-14 21:10
Category:Tech
Tags:Redis
Author:baijinping
Summary:对遇到过的Redis启动警告的一些情况分析和相应的应对方法

## 发现问题
------------
错误是在周三早上发生的。当时出现用户登录不了的情况，于是立即维护。

Redis 版本2.8。


## 分析问题
------------
检查日志后发现，在与Redis通信时所有的请求都抛出了如下异常：

	MISCONF Redis is configured to save RDB snapshots, but is currently not able to persist on disk. Commands that may modify the data set are disabled. Please check Redis logs for details about the error.

是Redis的快照行为出现错误，导致Redis拒绝执行请求。查看Redis的日志<马赛克了>，发现异常：

	......
	12 Aug | * 20000 changes in 600 seconds. Saving...
	12 Aug | * Background saving started by pid 6529
	12 Aug | * DB saved on disk
	12 Aug | * RDB: 100 MB of memory used by copy-on-write
	12 Aug | * Background saving terminated with success
	12 Aug | * 20000 changes in 600 seconds. Saving...
	12 Aug | # Can't save in background: fork: Cannot allocate memory
	12 Aug | * 20000 changes in 600 seconds. Saving...
	12 Aug | # Can't save in background: fork: Cannot allocate memory
	......

发生问题的直接原因是，在某一次Redis进行RDB备份的时候，由于申请不到足够的内存，导致备份失败，然后就一直拒绝处理请求。


## 解决问题
------------
原因找到了，就是内存不足。而内存不足的元凶正是RDB行为。

Redis进行RDB备份时，借助列fock命令的copy on write机制，在生成快照时，将当前进程整个复制出来，fock出一个子进程，然后在子进程中将所有数据写入到新的RDB文件。由此产生的问题：

*	**进行RDB备份时，需要多消耗Redis访问所占用内存的1倍**
*	如果数据集庞大，那么将产生大量的I/O负载

这里就不讨论如何选择Redis备份方案，注重解决问题。
比如说这台服务器是1G内存，Redis服务已经使用了600M的内存。如果此时进行RDB备份，Redis向OS申请内存。而OS发现内存不足，就告诉Redis进程内存不够，于是备份失败。


## overcommit_memory警告
------------
按照正常逻辑，如果系统内存不足，就会开始分配虚拟内存，不至于发生这种问题。
通过查找资料发现，其他人也遇到过这个问题。最终发现与Linux内存分配策略的设置参数有关：**vm:overcommit_memory**。

在Redis启动日志的开头找到如下警告：

	WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.


### 内核参数overcommit_memory 
它指 内存分配策略:
	可选值：0、1、2：

*	0， 表示内核将检查是否有足够的可用内存供应用进程使用；如果有足够的可用内存，内存申请允许；否则，内存申请失败，并把错误返回给应用进程。
*	1， 表示内核允许分配所有的物理内存，而不管当前的内存状态如何。
*	2， 表示内核允许分配超过所有物理内存和交换空间总和的内存


了解了overcommit的意义之后，解决这个问题非常简单，按照日志提示将vm.overcommit_memory设为1即可。
有3种方式修改内核参数，但要有root权限：

1. 编辑/etc/sysctl.conf ，改vm.overcommit_memory=1，然后sysctl -p 使配置文件生效;
2. sysctl vm.overcommit_memory=1
3. echo 1 > /proc/sys/vm/overcommit_memory


内核参数修改之后，不需要重启OS，也不需要重启Redis服务，立即就会生效。


## THP警告
------------
启动时还可能遇到THP警告：

	WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.

查看参考[3]的资料可以得到比较细致的分析。
解决方法就是按照警告中说的：

1. echo never > /sys/kernel/mm/transparent_hugepage/enabled
2. 重启Redis服务


## TCP backlog设置警告
------------
启动时还可能遇到TCP backlog警告

	WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.

详细参考[4]和[5].

解决方法：
	echo 511 > /proc/sys/net/core/somaxconn


## 总结
------------
redis配置文件中有许多的配置项，某些配置项的取值还要考虑系统本身的参数配置。

配置一旦有问题，很容易出现预料不到的情况。还好启动时有警告提示，遇到时细心解决就好了。

一句话，redis的配置文件得重新过一遍了。


## 参考资料
------------
1. [有关linux下redis overcommit_memory的问题](http://blog.csdn.net/whycold/article/details/21388455)
2. [Redis 启动警告错误解决](http://skly-java.iteye.com/blog/2167400)
3. [redis做RDB时请求超时case](http://blog.csdn.net/chosen0ne/article/details/46625359)
4. [redis tcp-backlog配置](http://www.bubuko.com/infodetail-311772.html)
5. [TCP queue 的一些问题](http://jaseywang.me/2014/07/20/tcp-queue-的一些问题)



