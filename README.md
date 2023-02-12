# HuayuChatting-Bot (zh_cn)

**REedit from https://github.com/jack20081117/HuayuChatting** 

 ![code statistic](https://codeline-statistic.zmh-program.repl.co/repo/LemonQu-GIT/HuayuChatting-bot)

此项目即为 HuayuChatting-WebUI 的衍生版本

本项目基于 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 的 QQ 机器人及我们社长同志的 [HuayuChatting](https://github.com/jack20081117/HuayuChatting) 项目开发 

以 GPL-3 协议开源

## How to use your code

### 部署

可使用 [Anaconda3](https://www.anaconda.com) 及 git 进行部署

```bash
mkdir HuayuChatting
cd HuayuChatting-Bot
mkdir Bot
git clone https://github.com/LemonQu-GIT/HuayuChatting-Bot.git
cd HuayuChatting-Bot
conda create -n HuayuChatting-Bot python=3.10
conda activate HuayuChatting-Bot
pip install -r requirements.txt
```

转至 https://github.com/Mrs4s/go-cqhttp 的 Release 界面下载适配你电脑的 go-cqhttp执行文件，并将它存放在在 ```HuayuChatting\Bot``` 中并运行并部署你的 go-cqhttp

具体部署操作请查看 https://github.com/Mrs4s/go-cqhttp/blob/master/README.md

转至 ```HuayuChatting\HuayuChatting-Bot\core\config.json``` 并进行设置权限组及文件路径等操作

你的 HuayuChatting 目录看起来应该是这样的：

> HuayuChatting.
> ├─ bot
> │  ├─ data
> │  │  ├─ cache
> │  │  ├─ images
> │  │  │  └─ guild-images
> │  │  ├─ leveldb-v3
> │  │  ├─ videos
> │  │  └─ voices
> │  ├─ dumps
> │  └─ logs
> └─ HuayuChatting-API
>     ├─ core
>     │  ├─ templates
>     │  └─ yolov5_img
>     ├─ in
>     └─ out

#### Config.json

在 ```HuayuChatting-Bot\core\config.json``` 中

```json
{
	"permissions":{
		"Admin": [<QQID>], #填写数组类型的管理员QQ号
		"Users": ["Default"],
		"Experimental": [<QQID>], #填写数组类型的可用yolov5功能的QQ号
		"Ban": [<QQID>], #填写数组类型的被封禁的QQ号
		"Bot":[2854196310] #填写数组类型的机器人QQ号
	},
	"config":{
		"yolov5_path":"~\\yolov5", #填写yolov5路径
		"QQImgDownload":"~\\HuayuChatting-Bot\\core\\yolov5_img",  #填写yolov5下载图片路径
		"go-cqhttp_image_path":"~\\bot\\data\\images", #填写你cqhttp的images路径
		"botQID":<QQID> #填写机器人的QQ号
	}
}
```



至此，部署操作完成

### 运行

在命令行中运行 go-cqhttp 的可执行文件

以 Windows 为例

```
call bot\go-cqhttp_windows_amd64.exe
activate HuayuChatting-Bot
python HuayuChatting-API\core\bot.py
```

在命令行中看见 Bot Started 后

运行成功

机器人日志存储在 oops.log 中

由于为什么叫 oops，是因为我在调试机器人失败后一直会说 oops，故将加入的日志名称设为 oops.log

## 命令

### 可用命令 （需在命令前@你的机器人）

* weekchart <学号>
* weekpie <YYYY-MM-DD>
* agechart
* echo <message>
* checkgroup
* esu <24885> #只能恶俗我们的社长
* wiki

Only For **Admin** :

* os._exit()
* batch <command>
* <command>

Only For **Admin** and **Experimental** :

* yolov5 <image>

### yolov5

这个 bot 加入了 yolov5 的功能

需自行配置 [yolov5](https://github.com/ultralytics/yolov5) 详见 https://github.com/ultralytics/yolov5/blob/master/README.zh-CN.md
