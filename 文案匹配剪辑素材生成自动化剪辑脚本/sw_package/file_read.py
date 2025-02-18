import json
import os
import pandas as pd

def data_json(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        data_json = json.loads(f.read())
        return data_json
    


def xlsx_to_json(file_path):
    df = pd.read_excel(file_path)

    json_dataStr = df.to_json(orient='records', force_ascii=False, indent=4)
    json_data = json.loads(json_dataStr)
    for index, value in enumerate(json_data, start=1):
        value["ID"] = str(index)

    return json_data



def create_output_folder():
    """
    在当前工作目录下创建一个名为 'output' 的文件夹。
    如果该文件夹已存在，则不执行任何操作。
    """
    # 获取当前工作目录
    current_dir = os.getcwd()
    
    # 拼接输出文件夹的完整路径
    output_folder_path = os.path.join(current_dir, "output")
    
    # 检查文件夹是否存在，如果不存在则创建
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    
    return output_folder_path


