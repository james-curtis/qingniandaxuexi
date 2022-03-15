# 青年大学习批量阅读文章的Python实现

在pc伪装微信浏览器并复制手机微信上的cookie登陆青年大学习页面，进行分析可知：
青年大学习API：dxx.hngqt.org.cn/study/studyAdd
温习青年大学习API：dxx.hngqt.org.cn/historystudy/studyHistoryAdd
阅读青年湖南说API：dxx.hngqt.org.cn/historystudy/studyHnProjectAdd
协议均为POST
参数均为projectId
经测试User-Agent可有可无，但是cookie中的sessionid必须要有。

具体sessionid获取方法如下：
在微信中操作
第一步.打开这个链接debugmm.qq.com/?forcex5=true点开后，退出就行了，接着下一步
第二步.打开这个网页debugx5.qq.com，安装线上内核网页链接
最上方大字，点信息
![img](http://qzonestyle.gtimg.cn/qzone/em/e401112.gif)打开vConsole调试功能，退出
第三步,打开青年大学习
第四步,点右下角绿色的vConsole,点击Storage选项卡,看到Cookies子选项卡,下面有个Name-Value键值对,下面有sessionid的具体值,长按复制即可

PS：积分更新有延迟，大概几小时。
自己的sessionid一定不要泄露了，不然别人可以直接登录你账号
下面讲一下手机使用方法(由于本人android没学好所以没写成安卓APP还浪费了两三个小时T﹏T，就用Python替代。用Python写还真特别简单)
1、在F-Droid里面下载termux，其他地方也可以(比如酷安)
2、打开安装Python，pkg in git wget python
3、安装requests库，pip install requests
4、复制脚本到/data/user/0/com.termux/files/home/，就是termux命令行里面输入pwd后显示的路径
5、输入python main.py即可
快进，在看视频页面打开vConsole输入document.getElementById('Bvideo').playbackRate=2，其中2为播放倍数
跳过，document.getElementById('Bvideo').currentTime=9999代码中9999是跳过的秒数，只要大于青年大学习的秒数就可以，需要输入两遍代码，第一遍答题，第二遍跳视频
12.10更新
无root复制文件到termux中
1、输入termux-setup-storage，获取内部储存使用权
2、cd ~，回home目录
3、找到你下载好的压缩包，解压，找到main.py的绝对路径，
例如我的是/storage/emulated/0/ADM/main.py，
输入cp /storage/emulated/0/ADM/main.py ./
复制到当前目录下
4、没了，复制完成，可以执行了(已经安装了Python和requests库的前提下)
12.16更新
修改教程
12.20更新
新增批量抽奖
优化逻辑
混淆加密
termux带资源包， https://yunling.lanzous.com/i6WRLj7vfah 
mt管理器(管理文件的)， https://yunling.lanzous.com/iVkCCj7vfna 
部分Linux命令:
ls列出当前目录下文件
pwd显示当前目录

# 截图

![image.png](http://tva1.sinaimg.cn/large/008d89Swgy1h0ax4yubppj311y0kgtjt.jpg)



![image.png](http://tva1.sinaimg.cn/large/008d89Swgy1h0ax4v29wwj311y0kgdtg.jpg)



![image.png](http://tva1.sinaimg.cn/large/008d89Swgy1h0ax4ovtjjj30u01t0470.jpg)



![image.png](http://tva1.sinaimg.cn/large/008d89Swgy1h0ax4ixdv0j30u01t0jza.jpg)



![image.png](http://tva1.sinaimg.cn/large/008d89Swgy1h0ax45n06jj30hs12jgwu.jpg)

