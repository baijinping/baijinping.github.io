Title:Redis RDB出错问题的分析
Date:2016-01-20 21:30
Category:Tech
Tags:Redis
Slug:redis-rdb-oom-error
Author:baijinping
Summary:一则Redis执行RDB出错的分析


### 无法执行redis更新操作

连接redis的应用程序在某段时间内，所有尝试写入redis操作均抛出如下异常：

	ResponseError: 
	MISCONF Redis is configured to save RDB snapshots, but is currently not able to 
	persist on disk. Commands that may modify the data set are disabled. Please check 
	Redis logs for details about the error.

根据提示检查redis日志，发现如下记录：

	22:55:27.011 * 99 changes in 99 seconds. Saving...
	22:55:27.117 * Background saving started by pid 7815
	22:56:25.524 # Background saving terminated by signal 9      <<<注意这一行
	22:56:25.631 * 99 changes in 99 seconds. Saving...
	22:56:25.730 * Background saving started by pid 7845
	22:57:03.879 * DB saved on disk
	22:57:03.997 * RDB: 2000 MB of memory used by copy-on-write
	22:57:04.651 * Background saving terminated with success

从上面几行redis日志可以看出，这段时间内进行了两次bgsave操作。第一次操作时，由于fork出来执行snapshot的进程(pid:7815)接收到linux 信号9（SIGKILL），进程关闭，从而失败了。redis紧接着又尝试了一次(pid:7845)才成功。

上面应用程序抛出异常的时间在进程(pid:7815)被干掉开始，直到第二次rdb成功结束。由此确定异常是由于bgsave失败，redis主动关闭所有更新操作并再次尝试执行bgsave。redis此举是为了将这种异常暴露出来，告知用户redis的持久化出现了问题。

通过修改redis启动配置中的**stop-writes-on-bgsave-error**项为**no**，可以避免在rdb失败时无法进行更新操作的行为。

	stop-writes-on-bgsave-error no

### bgsave失败原因
---

接下来寻找第一次rdb会失败的原因。
这台服务器的内存比较紧张，单个redis就占用了大半内存。从日志中可以看出，在进行此次rdb时，使用了许多额外的内存（2500MB），加上redis本身用到的内存，超过了服务器的物理内存。考虑到使用swap分区的可能，也一同检查了swap分区的大小。结果发现，swap分区大小仅有500MB。

在这种情境下，当时操作系统很有可能已经**无内存可分配**。

检查系统日志/var/log/messages发现如下记录：

	22:56:24 localhost kernel: irqbalance invoked oom-killer: gfp_mask=0x280da, order=0, oom_score_adj=0
	22:56:24 localhost kernel: irqbalance cpuset=/ mems_allowed=0
	......
	22:56:24 localhost kernel: Free swap  = 0kB
	......
	22:56:24 localhost kernel: Out of memory: Kill process 7815 (redis-server) score 516 or sacrifice child
	22:56:24 localhost kernel: Killed process 7815 (redis-server) total-vm:4520288kB, anon-rss:4376284kB, file-rss:32kB
	22:56:24 localhost kernel: redis-server: page allocation failure: order:0, mode:0x2015a

显然，当时由于无物理内存可供分配，用到了swap分区。但最终swap还是没能提供足够的空间（Free swap = 0kB），使得操作系统触发了OOM Killer机制，干掉了当前OOM的罪魁祸首（正在进行rdb的7815进程）。

那为什么第二次就成功了呢？大概是运气吧。

### 处理办法
---

整个问题基本分析清楚了，需要解决问题的话只有四个字：**加大内存**。

ps:整个分析过程还涉及到两块知识点，这里不深究：

* redis的rdb持久化的机制、fork机制
* Linux的OOM机制

### 参考
---

* [MISCONF Redis is configured to save RDB snapshots](http://stackoverflow.com/questions/19581059/misconf-redis-is-configured-to-save-rdb-snapshots)
* [Linux 的 Out-of-Memory (OOM) Killer](http://dbanotes.net/database/linux_outofmemory_oom_killer.html)
