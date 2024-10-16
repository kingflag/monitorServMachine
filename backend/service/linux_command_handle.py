import paramiko


def ssh_with_sudo_by_pwd(remote_host, remote_port, username, password, linux_command):
    # 创建一个新的 SSH 客户端
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # 连接到主机
        client.connect(hostname=remote_host, port=remote_port, username=username, password=password)

        # 打开一个会话并请求伪终端
        transport = client.get_transport()
        session = transport.open_session()
        session.get_pty()  # 请求伪终端
        session.exec_command(f"sudo -S {linux_command}")

        # 发送密码并加上换行符
        stdin = session.makefile('wb', -1)
        stdout = session.makefile('rb', -1)
        stderr = session.makefile_stderr('rb', -1)

        stdin.write(password + '\n')
        stdin.flush()

        # 读取输出和错误信息
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')
        if error:
            print("Error:", error)
            return error
        else:
            print("Output:", output)
            return output

    finally:
        client.close()
