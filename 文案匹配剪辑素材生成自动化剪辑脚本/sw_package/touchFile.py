import os 
import json
from sw_package.file_read import create_output_folder
def touch_folder_files_dictFile(root_dir):
    # 初始化一个字典来存储结果
    folder_files_dict = {}
    

    # 遍历根目录
    for root, dirs, files in os.walk(root_dir):
        # 如果当前目录下没有子目录，则认为是最底层文件夹
        if not dirs:
            # 去掉指定的前缀
            cleaned_root = root.replace(root_dir, "")
            # 将当前目录路径作为键，文件列表作为值
            folder_files_dict[cleaned_root] = files

            

        
    fileName = root_dir.rstrip("/").split("/")[-1] + ".json"
    filePath = os.path.join(create_output_folder(), fileName)
    print(filePath)
    with open(filePath, "w", encoding="utf-8") as json_file:
         json.dump(folder_files_dict, json_file, ensure_ascii=False, indent=4)    


    





