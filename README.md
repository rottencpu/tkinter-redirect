# tkinter-redirect

#### 介绍
python tkinter 打包脚本

#### 软件架构

```
python3.7
```


#### 安装教程

```
# 安装依赖
pip install -r requirements.txt
# 填写配置文件
# 测试运行
python main.py
# 使用pyinstaller打包
```

#### pyinstaller打包说明

```
pyinstaller -F -w -i assets/logo.ico main.py
# -F 独立文件打包
# -w 不显示终端
# -i + 路径.ico (制定icon)
PS: 如果有资源和配置文件，需要单独放入dist同级目录下 
```

#### 配置文件

```
{
    "path":"nginx.conf", # 需要替换的文件路径
    "host":"127.0.0.1", # 服务器地址
    "port":22, # 端口
    "user":"root", # 账号
    "passwd":"passwd", # 密码
    "up_pwd":"/root/",  # 上传路径
    "cmd":"ls", # 服务端指令,多个指令 ';' 隔开
    "old_ip":"127.0.0.2" # 第一次使用,需要填写,便于匹配
}
```