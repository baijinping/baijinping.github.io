Title:linux下手动添加python自定义库
Date:2015-08-26 22:44
Category:Tech
Tags:Python
Author:baijinping
Summary:添加python自定义库，避免每次使用都要手动添加到sys.path

## 问题情境
------------
linux中手动添加python库路径：

1. 添加自定义库；
2. 升级了小版本py，引入之前的库

## 解决步骤
------------

1. 首先确定当前py标准库的存放路径：命令行中打印os库，就可以得到路径；
2. 在site-packages/目录下创建一个路径配置文件，如mypath.pth，必须以.pth为后缀；
3. 编辑mypath.pth，将需要添加的库的所在路径添加到pth文件中即可。每个路径单独放一行；
4. 重启python，就可以发现sys.path已经将pth文件中的路径包含进来了。

### ps：

1. 对于egg文件夹，需要导入egg，方便引入egg下面实际的lib名称相同的文件夹;
2. 若site-packages下的文件名和库名相同，则不需要导入，因为site-packages会包含它.
