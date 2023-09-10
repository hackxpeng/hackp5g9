# LET'S HACK NOW!
本项目可以帮助小鹏P5和小鹏G9开启adb和网络adb

# 开启adb步骤
* 首先确认您的爱车是小鹏P5（所有系统版本）或小鹏G9（所有系统版本）或小鹏G6（所有系统版本）或小鹏P7（OTA2.10及之前）或小鹏G3（版本不确定，最新版不行）
* 将您的笔记本电脑（已安装adb组件）或安卓手机（已安装甲壳虫adb软件）和您的车机连接到同一无线局域网中（此处可使用另一台手机打开热点），以下使用笔记本电脑举例
* 打开车机的拨号界面，输入`*#9925*111#* `
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
* 将P7 P5的地图更新到高德地图最新版本（包括红绿灯倒计时，最新版高精地图，组队功能，普通道路沉浸导航，语音包等）

* 将P7 P5的QQ音乐更新到最新版本

* 承诺定期公布OTA进度（最低界限为每月公布）

* 将P5 p版sr下放到e版车型（显示车辆运动轨迹）

* 优化P7 P5 G3/i自动泊车

* 优化NGP并将速度上限设置为130

* 将P7 P5的夜晚/白天切换逻辑修改为根据光线传感器，而非日出日落时间

* 重新评估P7 P5适配新版UI的可行性

* 重新评估P7更换8155车机的可行性

* 全部完成后使用小鹏汽车官方Github账号在本仓库发送issue

  

![image](https://ghproxy.com/https://raw.githubusercontent.com/hackxpeng/hackp5g9/main/699e33d95bb58866f263e99946870d0f.jpeg)
