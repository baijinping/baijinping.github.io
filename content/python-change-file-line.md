Title:python超简约替换文件字符串 
Date:2014-11-16 10:05
Category:Tech
Tags:Python
Slug:python-change-file-line
Summary:python-文件字符串替换（超简约）

这里使用了re库。

    :::python
    #encoding:utf8
    """
    实现修改某一文件中,包含指定子串的行,替换为指定字符串
    """
    import re;
    def changeFileLineToNew(filePath, strToFind, strToReplace):
        "修改后直接覆盖源文件"
        with open(filePath) as f:
            content = f.read();
        #关键是下面这行
        # 打开源文件，都出来用re进行字符串替换，然后保存到源文件中
        open(filePath, "w").write(re.sub(strToFind, strToReplace, content));
        pass
        
    def test():
        changeFileLine("adMod.lua", "local reqUrl", "local reqUrl = '192.168.1.1'");
        pass
        
    if __name__ == '__main__':
        test()

