import re
import paramiko
from time import sleep


# 验证IP是否有效
def matchIP(ip):
    if re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip):
        return ip

# 服务器 - 上传文件 (config 必须是个dict)
def scpServer(BASE_DIR, config):
    path = BASE_DIR + '\\config\\' +config['path']
    print('上传文件:\n' + path)
    transport = paramiko.Transport((config['host'], config['port']))
    transport.connect(username=config['user'], password=config['passwd'])
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(path, config['up_pwd']+config['path'])
    transport.close()
    print('上传文件成功')

# 服务器 - 发送指令 (config 必须是个dict)
def cmdServer(config):
    print("发送指令...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=config['host'], port=config['port'], username=config['user'], password=config['passwd'])
    cmd = config['cmd']
    stdin, stdout, stderr = ssh.exec_command(cmd)
    result = stdout.read()
    if not result:
        result = stderr.read()
    ssh.close()
    print("终端返回信息：\n{}".format(result.decode()))

# 程序结束操作
def ending():
    print('程序结束,请主动退出...')
    while True:
        sleep(1)