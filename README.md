## Chatter

Chatter 是一个简单的微信聊天机器人

* 聊天功能的实现基于`itchatter`，通过调用web微信的方式实现和人以及群的聊天。
* 智能化回复基于`chatterbot`， 它自带一些聊天的数据用于训练，此外它还能够在后续的聊天中继续学习并且变得更加智能化。

### 安装

* `mv config.py.sample config.py`
* 编辑config.py，填入你*准确*的昵称
* pip install -r requirements.txt

### 使用

`python main.py`启动程序即可。首次运行需要下载训练用的数据，会比较慢。

* 扫描机器人的二维码，即可立即被添加为好友。
* 可以直接与机器人对话。
* 也可以在群聊里面@机器人的昵称与它互动。
* 群聊里面不@机器人昵称则不会收到机器人的回复，但是聊天记录依然会被用于机器人的学习