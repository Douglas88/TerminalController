## TerminalController
windows/Linux(理论支持Mac) 远程管理：屏幕监控（win）、键盘记录（linux 需root权限）、文件管理、命令执行
### 
    逻辑代码分离，客户端连到服务器才下发逻辑代码，后期可动态更新客户端功能，而不需要重新下载编译
### 项目仍在开发中... 进度 9/10
#### 目前可以使用的功能：
    屏幕监控、键盘记录、文件管理（上传、遍历、在线编辑、删除、重命名、下载、解压缩zip）、命令执行
### 关于运行(运行的机器需要python3.6+)
    git clone https://github.com/mycve/TerminalController.git
    cd TerminalController/server
    python -m pip install -r requirements.txt
    python server.py
    

### 关于构建客户端说明
    linux客户端依赖python3的环境，点击主页右下加创建，输入服务器地址（默认打开的URL），可以直接生成在buildout目录
    windows输入服务器地址点击创建后，在点击目录下的build.cmd，在弹出的界面（非web弹出）一直点下一步（调用win系统自带打包工具），等待打包完，到buildout目录
    你也可以复制server下的app.py到client目录下，并修改服务器地址如：SERVER_ADDRESS = "https://xxx.com",接着到linux、win使用`pyinstaller -F client/app.py` 打包可执行文件(如果你看不懂这句话，参考下面Pyinstaller)
### [Pyinstaller](http://c.biancheng.net/view/2690.html)

### 关于项目结构
    buildenv打包依赖
    buildout可执行文件的输出目录
    client可执行存放代码
    server服务端
        server.py 服务端启动入口
        config.py （全局你只需要关心这个配置文件）SPEED=3 代表截屏速度每3秒1次，最好不要小于0.7左右
        app.py 客户端待打包入口文件，打包时会复制一份到client下
        base.py 客户端后期动态加载的逻辑代码
        requirements.txt 服务端依赖库清单
        static 静态文件，存放对方拉回的文件，web的ui，css，js等
        templates 存放web界面模板
    build.cmd windows编译可执行文件打包

<img alt="image" height="300" src="https://github.com/mycve/TerminalController/raw/main/1.png" width="1400"/>
<img alt="image" height="300" src="https://github.com/mycve/TerminalController/raw/main/2.png" width="1400"/>

### 免责、版权声明（浏览、下载=代表同意条款）
    此工具作用于合规合法的攻防演练，或其它（包括不限于 教育、学习等目的）
    开发者享有最终解释权、任何分歧等问题、以开发者解释为准。
