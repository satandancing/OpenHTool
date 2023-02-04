#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-25 上午11:56
# @Update  : 01-03-2023
# @Author  : VectorWei
# @Email   : satandancing@gmail.com
# @Site    :
# @File    : pyRenderCmd.py
# @Software: PyCharm
import hou
import platform

tt = hou.selectedNodes()
sysName = platform. system().lower()

types = [
    'prepost',
    'framedep',
    'wedge',
    'fetch',
    'merge',
    'null'
]

if (len(tt) == 0):
    if hou.ui.displayMessage(
            "Select Rop Node and retry!\n选择ROP节点之后重试！",
            buttons=(
                "OK",
            )) == 0:
        print('Eror')

else:
    hipFile = hou.hipFile.path()
    sel = hou.selectedNodes()[0]
    path = hou.Node.path(sel)
    type = sel.type().name()
    
    if type in types:
        print("echo render -V {}|hbatch {}".format(path, hipFile))
        if sysName == 'darwin' or sysName == 'linux':
            hou.ui.displayMessage(
                "View the rendering command line of the output in the Python Shell panel!\n在Python Shell面板查看输出的渲染命令行！",
                buttons=(
                    "OK",
                ))
        else:
            pass
    else:
        vfg = sel.parm('trange').eval()
        if vfg == 0:
            print("echo render -V {}|hbatch {}".format(path, hipFile))
            if sysName == 'darwin' or sysName == 'linux':
                hou.ui.displayMessage(
                    "View the rendering command line of the output in the Python Shell panel!\n在Python Shell面板查看输出的渲染命令行！",
                    buttons=(
                        "OK",
                    ))
            else:
                pass
        else:
            f1 = int(sel.parm('f1').eval())
            f2 = int(sel.parm('f2').eval())
            
            print("echo render -V -f {} {} {}|hbatch {}".format(
                f1, f2, path, hipFile))
            if sysName == 'darwin' or sysName == 'linux':
                hou.ui.displayMessage(
                    "View the rendering command line of the output in the Python Shell panel!\n在Python Shell面板查看输出的渲染命令行！",
                    buttons=(
                        "OK",
                    ))
            else:
                pass