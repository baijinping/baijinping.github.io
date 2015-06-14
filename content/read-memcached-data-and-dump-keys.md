Title:实时查看memcache中的数据
Date:2014-12-12 14:30
Category:Tech
Tags:NoSQL
Slug:read-memcached-data-and-dump-keys


---

####memcache命令

可用telnet与memcache进行通信：

`telnet {:hostname} {:port}`

memcache的通信协议是简单文本行。使用get key可以查看对应key的值。

memcache中查看数据时常用的命令：

* `stats` 查看状态信息
* `stats items` 列出每个slabs的简要信息
* `stats slabs` 列出每个slabs的详细信息
* `stats cachedump {:slabNo} {:rowNo}` 列出rowNo个位于指定slabNo的记录的key，如果rowNo为0，表示列出所有
* `get {:key}` 获取指定key的数据


---

####关于获取memcache的所有key
我在网上专门查找过关于“获取及遍历memcache的所有key”这一问题的解决方案，但无一例外都是使用`stats cachedump`命令来获取的。这个简单易懂命令很容易让人忽略一个事实，那就是cachedump能获取到的内容的大小是有上限的，cache的大小是2M。

这意味着你无法确保cachedump能够将所有key导出。
当然，这比没有要好多了。

---

####参考

* [http://lzone.de/cheat-sheet/memcached#Dumping Memcache Keys](http://lzone.de/cheat-sheet/memcached#Dumping Memcache Keys)
* [http://lists.danga.com/pipermail/memcached/2007-April/003905.html](http://lists.danga.com/pipermail/memcached/2007-April/003905.html)
* [https://groups.google.com/forum/#!searchin/memcached/cachedump/memcached/UfCPP-yjvDU/RbD0K59VCykJ](https://groups.google.com/forum/#!searchin/memcached/cachedump/memcached/UfCPP-yjvDU/RbD0K59VCykJ)
