# HAPPY NEW YEAR!
本项目可以帮助历史版本的小鹏P5和小鹏G9开启adb和网络adb

# 重要提示
## 如果你对第三方软件的需求高于OTA需求，请关闭OTA功能，P5和G9的下一个版本大概率或已经启用了更高级的加密方式，无法获取解锁码，需要等待其他方式破解

## 讨论群：https://t.me/hackxpeng

# 开启adb步骤
* 首先确认您的爱车是小鹏P5（XMART OS 3.5.0及之前）或小鹏G9（XMART OS 4.3.1及之前）或小鹏P7（XMART OS 2.10及之前）

* 将您的笔记本电脑（已安装adb组件）或安卓手机（已安装甲壳虫adb软件）和您的车机连接到同一无线局域网中（此处可使用另一台手机打开热点），以下使用笔记本电脑举例

* 打开车机的拨号界面，输入`*#9925*111#*`

* 此时车机会显示一个页面，其中包含一个二维码

* 使用微信扫描您的车机的二维码，并将内容保存备用

* 在任意输入框中输入内容`https://hackxpeng.bgcpdd.eu.org/xpeng?m=hackxpeng&id=`，然后将您获取到的二维码内容复制到最后面，注意此处不要有任何的空格

* 使用浏览器打开您输入框中的所有内容（网址拼接，如：`https://hackxpeng.bgcpdd.eu.org/xpeng?m=hackxpeng&id=XPENGD55xxxxxxxxxxxxxx`）

* 浏览器返回一个解锁码（如：`*#03*12345678*#`）

* 将该解锁码输入车机的拨号界面，此时解锁码会自动消失，如果没有消失请手动删除所有内容

* 使用拨号界面输入`*#9387*141#*`

* 打开调试和网络调试（一般是前两个选项）

* 笔记本电脑使用`win+r`，输入`cmd`回车，输入`adb connect 车机页面中的ip:5050`（如`adb connect 172.20.10.2:5050`）

* cmd显示连接成功

* 下载你需要安装的apk

* 使用`adb install`安装软件（如：`adb install C:\abc\a.apk`）

* 安装成功

* adb还有更多好玩有趣的玩法等你发现

# 笔记本电脑安装adb套件
* 打开`https://developer.android.google.cn/studio/releases/platform-tools?hl=zh-cn`

* 下载windows版本 并解压

* 将所有文件放入c盘windows目录下的system32和syswow64 注意两个都要放


# 致小鹏汽车：以下是关闭获取解锁码api的步骤
* 暂无

  


![image](https://ghproxy.com/https://raw.githubusercontent.com/hackxpeng/hackp5g9/main/699e33d95bb58866f263e99946870d0f.jpeg)
