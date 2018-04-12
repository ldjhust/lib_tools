# -*- coding:utf-8 -*-

"""Python2 实现一些工具需求
"""

import hashlib


def get_sha1(filename):
    """获取基于文件内容的sha1值
    """
    
    # 文件需以二进制的方式读取，否则计算sha1时可能会出错
    with open(filename, "rb") as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        
        # 返回32位的十六进制哈希值
        return sha1obj.hexdigest()
