import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# 指定要列出的目录路径
directory_path = "/run/user/1000/gvfs/smb-share:server=xiawei.local,share=1号储存盘/SW速惟项目/sw文案架构成片/SW-AccountA-20250218A-SceneA-ModelA-S4SS1067-冰川灰-20250221-30-成片"


output_file_path = os.path.basename(directory_path)

# 打开输出文件，准备写入内容
with open(output_file_path, "w") as output_file:
    # 遍历指定目录
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            # 拼接完整的文件路径
            full_path = os.path.join(root, file_name)
            # 写入文件路径到输出文件
            output_file.write(full_path + "\n")

print(f"所有文件的完整路径已保存到文件: {output_file_path}")