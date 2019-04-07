import json
import requests
import os
# 自定义
from utils.common import matchIP, scpServer, cmdServer, ending
# 当前文件路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

url = 'http://ip.360.cn/IPShare/info'
ip = ''
config = {}


# 获取IP
def getIP():
    r = requests.get(url)
    res = json.loads(r.text)
    local_ip = matchIP(res['ip'])
    if local_ip:
        global ip
        ip = local_ip

# 获取本地的config.json配置文件
def getConfig():
    with open("config/config.json","r") as load_f:
        global config
        config = json.load(load_f)
        print('获取配置文件:\n' + str(config))

# 获取本地配置文件，进行对比替换
def getFile():
    print('对比文件...')
    if config['old_ip'] != ip:
        print('新IP:'+ ip +'与旧IP:'+ config['old_ip'] +'IP不一致，进行替换文本操作')
        path = 'config/'+config['path']
        txt = ''
        with open(path,"r") as f:
            txt = f.read()
        # 匹配旧IP替换新IP
        txt1 = txt.replace(config['old_ip'], ip)
        # 写入文件
        with open(path, 'w') as f:
            f.write(txt1)
        print('替换成功...')
        return True
    else:
        print('IP - 相同，不执行操作~')
        ending()
        return

# 替换配置文件
def updateConf():
    print('更新配置文件')
    new_config = config
    new_config['old_ip'] = ip
    with open('config/config.json', 'w') as conf:
        conf.write(json.dumps(new_config))
    print('更新配置文件 - ok')

# 主要程序入口
def main():
    """
    1.获取IP
    2.获取本地配置文件
    3.获取本地需要修改的文件比对操作
    5.将文件上传服务器
    6.发送指令
    7.全部完成，替换配置文件
    """
    getIP()
    getConfig()
    if getFile():
        instr = input("是否执行上传服务器操作 \nYes：任意输入，No：输入no: ")
        if instr != 'no':
            scpServer(BASE_DIR, config)
            cmdServer(config)
            updateConf()
            ending()
        else:
            ending()

if __name__ == '__main__':
    print('正在执行程序...\n')
    main()