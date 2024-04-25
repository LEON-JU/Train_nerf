import os

def rename_files(path, prefix):
    # 获取目录下所有的文件名
    file_list = os.listdir(path)
    
    # 遍历文件名
    for filename in file_list:
        # 判断文件是否为jpg格式
        if filename.endswith(".jpg"):
            # 提取序号
            index = filename.split("_")[1].split(".")[0]
            
            # 构建新的文件名
            new_filename = f"{prefix}_{index}.jpg"
            
            # 重命名文件
            os.rename(os.path.join(path, filename), os.path.join(path, new_filename))

# 调用函数进行重命名
rename_files("./data/desk", "images")
