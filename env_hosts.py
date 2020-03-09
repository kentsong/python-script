import os
import sys
import subprocess

def main():
    ### 1.确认命列列参数
    #print ('参数个数为:', len(sys.argv), '个参数。')
    #print ('参数列表:', str(sys.argv))
    
    flag_prod = True
    
    if len(sys.argv) > 1:
        #print(sys.argv[1])
        if sys.argv[1] == 'testing':
            flag_prod = False
            #print('argv ---> flag_testing='+str(flag_testing))
    
    ### 需要被维护的 ip 列表
    ip_dict = {
        '101.236.15.64':'api-oeco-itv.cp21.ott.cibntv.net',
        '10.124.65.105':'plugin-scloud.cp21.ott.cibntv.net'
    }
    
    '''
    写入'#'
    '''
    def checkFlag(line):
        return '#'+line if flag_prod else line
    
    '''
    w+打开文件会将原文件内容删除，可以同时对文件进行读写
    r+打开文件会保持原文件内容不变，同样可以同时对文件进行读写
    '''
    
    ### 2.检查line是否包含指定字段
    
    path = '/etc/hosts'
    data=[]
    for line in open(path, mode='r'):
        line = line.rstrip()
        for key in ip_dict:
            if line.find(key) != -1:
                line = checkFlag(key+' '+ip_dict[key])
        data.append(line)
    
    
    file = open(path, mode='w+')
    #寫入並加換行符號
    for line in data:
        file.write(line+os.linesep)
    #關閉文件    
    file.close()
    
    #hosts配置立即生效
    os.system('source /etc/hosts')
    print ('正式环境已生效' if flag_prod else '测试环境已生效')    

##检查sudo权限 
if os.geteuid() == 0:
    print("We're root!")
    main()    
else:
    print("We're not root.")
    subprocess.call(['sudo', 'python3', *sys.argv])
    sys.exit()




  