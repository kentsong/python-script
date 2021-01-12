import os
import sys
import subprocess


# https://blog.csdn.net/qq_27825451/article/details/102909772

def main():
    if len(sys.argv) > 1:
        # print(sys.argv[1])
        if sys.argv[1] == 'testing':
            print('测试环境已生效')
            print(subprocess.call("adb push host_files/hosts_testing /system/etc/hosts", shell=True))  # shell参数为true，则，命令以及参数以字符串的形式给出
    else:
        print('正式环境已生效')
        print(subprocess.call("adb push host_files/hosts /system/etc/hosts", shell=True))  # shell参数为true，则，命令以及参数以字符串的形式给出


main()