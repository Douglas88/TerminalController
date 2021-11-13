## TerminalController
windows/Linux(理论支持Mac) 远程管理：屏幕监控（win）、键盘记录（linux 需root权限）、文件管理、命令执行
### 
    逻辑代码分离，客户端连到服务器才下发逻辑代码，后期可动态更新客户端功能，而不需要重新下载编译
### 项目仍在开发中... 进度 9/10
#### 目前可以使用的功能：
    屏幕监控、键盘记录、文件管理（上传、遍历、在线编辑、删除、重命名、下载、解压缩zip）、命令执行

### 关于构建
    linux需要python3的环境，点击主页右下加创建，输入服务器地址，可以直接生成在buildout目录
    windows需要输入服务器地址点击创建后，在点击目录下的build.cmd，在弹出的界面一直点下一步，等待打包完，到buildout目录
    你也可以复制server下的app.py到client目录下，并修改服务器地址如：SERVER_ADDRESS = "https://xxx.com",接着到linux、win使用`pyinstaller -F client/app.py` 打包可执行文件
### 
    启动服务器进入到server目录 执行 python server.py，当然你可以修改里面的端口PORT，截图速度SPEED。

### 免责、版权声明（浏览、下载=代表同意条款）
    此工具作用于合规合法的攻防演练，或其它（包括不限于 教育、学习等目的）
    开发者享有最终解释权、任何分歧等问题、以开发者解释为准。
