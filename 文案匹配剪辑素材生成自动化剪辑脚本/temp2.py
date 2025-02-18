

import os
import json

def get_files_in_lowest_folders(root_dir):
    # 初始化一个字典来存储结果
    result = {}

    # 遍历根目录
    for root, dirs, files in os.walk(root_dir):
        # 如果当前目录下没有子目录，则认为是最底层文件夹
        if not dirs:
            # 去掉指定的前缀
            cleaned_root = root.replace(root_dir, "")
            # 将当前目录路径作为键，文件列表作为值
            result[cleaned_root] = files

    return result

# 示例文件夹路径
root_dir = "/run/user/1000/gvfs/smb-share:server=xiawei.local,share=1号储存盘/SW速惟项目/视频素材库/SW/SW-AccountA-20250218A-SceneA-ModelA-S4SS1067-青柠绿/"
last_part = root_dir.rstrip("/").split("/")[-1]
# for i in last_part:
#     print(i)

print(last_part)

# 获取最底层文件夹及其文件
folder_files_dict = get_files_in_lowest_folders(root_dir)

# 将字典写入 JSON 文件
output_file = "folder_files_dict.json"
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(folder_files_dict, json_file, ensure_ascii=False, indent=4)

print(f"字典已成功写入到文件 {output_file}")


# 铁锈红/产品整体画面/模特展示/动态展示/S&W1a2b3c4d.mp4
# 铁锈红/产品体验画面/亲肤柔软/S&W5e6f7g8h.mp4
# 铁锈红/产品风格画面/慵懒风/S&W3m4n5o6p.mp4
# 铁锈红/产品细节画面/产品展示/优雅小圆领/S&W1u2v3w4x.mp4
# 铁锈红/产品整体画面/模特展示/动态展示/S&W9c0d1e2f.mp4