# @Author: ZhangKe
# @Email: zk1575595743@163.com
# @Create Time: 2020-09-06 16:54
# @last Update Time: 2020-09-06 16:54
# @Dec: 输入文件夹地址，文件起始编号，实现文件重命名

import os

path = input("请输入文件夹的绝对路径:\n")
count_str = input("请输入文件的起始编号:\n")
print("重命名开始！\n")
count = int(count_str)
_fileList = os.listdir(path)
for file in _fileList:
    oldDir = os.path.join(path,file)
    if os.path.isdir(oldDir):
        continue
    fileName = os.path.splitext(file)[0]    # 文件名
    filetype = os.path.splitext(file)[1]    # 扩展名
    newDir = os.path.join(path, str(count)+filetype)
    os.rename(oldDir, newDir)
    count = count + 1
print("重命名完成！")

