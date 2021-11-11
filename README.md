## TerminalController
windows/Linux(理论支持Mac) 远程管理：屏幕监控（win）、键盘记录（linux 需root权限）、文件管理、命令执行
### 
    逻辑代码分离，客户端连到服务器才下发逻辑代码，后期可动态更新客户端功能，而不需要重新下载编译
### 项目仍在开发中... 进度 9/10
#### 目前可以使用的功能：
    屏幕监控、键盘记录、文件管理（上传、遍历、在线编辑、删除、重命名、下载、解压缩zip）、命令执行

### 客户端构建可执行文件时创建新的环境 进入虚拟环境后执行
    (venv) E:\xxxxxx\WinController\client>build.cmd
### 当然，你也可以自己编译，如果有点基础的话
#### 
    1. server 放在服务端启动即可【 SPEED 代表每秒截屏/次 PORT=监听端口】
    2. client 可以自己编译单文件执行 -> 具体看pyinstaller使用手册
    3. client中app.py修改SERVER_ADDRESS为自己域名，nginx反代的话nginx需要配置websocket，百度一下

#### client文件夹下文件，可以压缩成zip，放到linux、win通过 `python3 xxx.zip`执行 
    Tips: python可以执行zip压缩包文件


![image](https://github.com/mycve/WinController/blob/main/1.png)
![image](https://github.com/mycve/WinController/blob/main/2.png)
![image](https://github.com/mycve/WinController/blob/main/3.png)


[演示视频](https://github.com/mycve/WinController/blob/main/demo.mp4?raw=true)

### 免责、版权声明（浏览、下载=代表同意条款）
    此工具作用于合规合法的攻防演练，或其它（包括不限于 教育、学习等目的）
    开发者享有最终解释权、任何分歧等问题、以开发者解释为准。
