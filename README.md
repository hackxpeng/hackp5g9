## 最新教程（适用于所有使用天玑风味系统及XMART OS系统的车辆） https://t.me/hackxpeng

# 敬告小鹏相关部门：如果不妥善处理P5/G3i车型后续更新，我们将会公布车机ROOT教程

- 首先，你需要PY一下售后门店，请求进入维保模式

- 进入维保模式后，进入常用指令界面，在第一个输入框输入以下代码：

  `ro.product.model;am start com.xiaopeng.devtools/.view.usersettings.UserSettingsActivity`

  即可打开调试和网络调试（一般是前两个选项），请注意所有的符号请使用英文输入

- 其余步骤请参考历史教程即可





# 以下是历史教程，最新版本天玑风味系统已修复

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


# 致何小鹏：NMSL

![image](https://raw.githubusercontent.com/hackxpeng/hackp5g9/refs/heads/main/699e33d95bb58866f263e99946870d0f.jpeg)
