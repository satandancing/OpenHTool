#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-3 10:02
# @Update  : 01-15-2023
# @Author  : VectorWei
# @Email   : satandancing@gmail.com
# @Site    :
# @File    : pyRenderList.py
# @Software: PyCharm

import os
import platform

hipFile = hou.hipFile.path()
floder_path = hou.hscriptExpression("$HIP")
file_name = "RenderList.cmd"
file_path = floder_path + '/' + file_name
sysName = platform. system().lower()


if os.path.exists(file_path):
    os.remove(file_path)
else:
    pass

HOU_MANTRA_NODE_TYPE = [
    "ifd",
    "karma"
]

for i in HOU_MANTRA_NODE_TYPE:
    # HOU_MANTRA_NODE_TYPE = "ifd"
    node_type = hou.nodeType(hou.ropNodeTypeCategory(), i)
    render_node_type = node_type.instances()

    if render_node_type == ():
        hou.ui.displayMessage(
            'A renderable node could not be found for the current file!\n当前文件无法找到可渲染的节点！',
            buttons=(
                'OK',
            ))
        break
    else:
        for i in render_node_type:
            render_node_path = hou.Node.path(i)
            mode = 'a' if os.path.exists(file_path) else 'w'
            with open(file_path, mode) as f:
                f.write("mread {};\n".format(hipFile))
                f.write("render -V {};\n".format(render_node_path))
                f.close()

if os.path.exists(file_path):
    if sysName == 'darwin' or sysName == 'linux':
                hou.ui.displayMessage(
                    "View the rendering command line of the output in the Python Shell panel!\n在Python Shell面板查看输出的渲染命令行！",
                    buttons=(
                        "OK",
                    ))
                print(("Copy the following command into Houdini Terminal to execute the render!\n拷贝下列命令到Houdini Terminal中执行渲染！\n\nhscript {}").format(file_path))
    else:
        pass