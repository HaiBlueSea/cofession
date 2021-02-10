import os
import re

def get_new_name(files):
    '''@files 
    '''
    # def clean(string):
    #     ##去除空格
    #     temp = string.replace(' ','')
    #     p1 = "\(.+?\)"
    #     return re.sub(p1, "", temp)
    return ['幻灯片'+ str(i+1) + '.jpg' for i,old in enumerate(files)]


def re_name(path):
    '''重新命令path下文件的名字
    '''
    files = os.listdir(path)
    old_name = [i for i in files if 'jpg' in i]
    new_name = get_new_name(old_name)
    
    for i in range(len(old_name)):
        if old_name[i] != new_name[i]:
            os.rename(os.path.join(path,old_name[i]), os.path.join(path,new_name[i]))

if __name__ == '__main__':
	path = os.getcwd()
	re_name(path)