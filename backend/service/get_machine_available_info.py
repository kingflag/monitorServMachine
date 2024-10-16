from backend.service import linux_command_handle as my_command


def get_cpu_usage_rate(ip_address, user_name, password):
    cpu_command = "sudo mpstat 1 1 | awk '/all/ {usage=100-$NF} END {print usage}'"
    print(f'cpu_command:{cpu_command}')
    cpu_rate = my_command.ssh_with_sudo_by_pwd(ip_address, 22, user_name, password, cpu_command)
    print(f'cpu_rate:{cpu_rate}')
    return cpu_rate


def get_mem_usage_rate(ip_address, user_name, password):
    mem_command = "sudo awk '/MemTotal:/{total=$2}/MemFree:/{free=$2}/Buffers:/{buffers=$2}/Cached:/{cached=$2} END {" \
                  "used=total-free-buffers-cached; print  used/total * 100.0}' /proc/meminfo"
    print(f'mem_command:{mem_command}')
    mem_rate = my_command.ssh_with_sudo_by_pwd(ip_address, 22, user_name, password, mem_command)
    print(f'cpu_rate:{mem_rate}')
    return mem_rate
