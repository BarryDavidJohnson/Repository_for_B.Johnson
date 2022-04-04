import sys
import os
from tkinter import *
from you_get import common as you_get
#import you_get

class websiteprompt:
    def __init__(self,url,path=''):
        self.url=url
        self.path=path
        self.path=str(self.path).replace('\\',os.sep)
        self.path=str(self.path).replace('/',os.sep)
        if str(self.path)[-1]==os.sep:
            pass
        elif str(self.path)[-1]==' ':
            while True:
                self.path=str(self.path)[:-1]    #切除最后一个字符
                try:
                    if str(self.path)[-1]==' ':
                        continue
                    elif str(self.path)[-1]==os.sep:
                        break
                    else:
                        self.path=str(self.path)+os.sep
                        break
                except:
                    break
        else:
            self.path=str(self.path)+os.sep
        self.path=str(self.path)[:-1]
    @property
    def getpath(self):
        return self.path
    @property
    def geturl(self):
        return self.url
def running():
    prompt=websiteprompt(addressE.get(),pathE.get())
    dictionary=prompt.getpath
    url=prompt.geturl
    sys.argv=['you-get','-o',dictionary,url]
    '''
    for i in range(len(sys.argv)):
        print(sys.argv[i],end=' ')
    '''
    you_get.main()
def ending():
    sys.exit()
if __name__=='__main__':
    root=Tk()    #初始化GUI环境

    root.title('bilibili视频下载工具')    #GUI窗口标题
    
    #输入框标签及定位
    separate0 = Label(root,text=' ',font=("宋体",6))
    separate0.grid(row=0)

    addressL = Label(root, text="视频地址",font=("宋体",18))
    addressL.grid(row=1)
    addressE = Entry(root,font=("宋体",18))
    addressE.insert(0,'')
    addressE.grid(row=1, column=1)

    separate1 = Label(root,text=' ',font=("宋体",6))
    separate1.grid(row=2)

    pathL = Label(root, text="保存目录",font=("宋体",18))  
    pathL.grid(row=3)
    pathE = Entry(root,font=("宋体",18))
    pathE.insert(0,'')
    pathE.grid(row=3, column=1)

    separate2 = Label(root,text=' ',font=("宋体",6))
    separate2.grid(row=4)

    #运行按钮标签及定位,操作函数不能含有形参,不可用@property修饰变为属性
    runBtn = Button(root, text="下载", command=running,font=("宋体",12))
    runBtn.grid(row=5, column=0, sticky=W, pady=5)
    quitBtn = Button(root, text="退出", command=ending,font=("宋体",12))
    quitBtn.grid(row=5, column=3, sticky=W, pady=5)

    #Tk()模块主程序循环,定义在tkinter模块中
    root.mainloop()

