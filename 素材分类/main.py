
import os
import json 
from openai import OpenAI

def create_directories_from_string(dir_string):
    # 按行分割字符串
    lines = dir_string.strip().split('\n')
    
    # 遍历每一行
    for line in lines:
        # 去掉行前的空格，以确定文件夹的深度
        line = line.lstrip()
        
        # 创建文件夹
        # 这里使用了相对路径，以当前工作目录为基准
        os.makedirs(line, exist_ok=True)  # exist_ok=True 表示如果文件夹已经存在，不会抛出异常
    
    print("素材文件夹创建完成！")

def chat_request(question):
    client = OpenAI(
       base_url="http://aiagent-pre.chengwen.net/api/v1",  
       api_key="prechengwenai-tpT9jAcdDdRVXl8nPJtkiNkUYK2Zklbw1kgUxCmaNKJh0oisbkRQIS"
    )
    
    completion = client.chat.completions.create(
        model="doubao-pro-128k",
        messages=[{'role': 'user', 'content': f'{question}'}],
    )
    completion_cp = completion.model_dump_json()
    data = json.loads(completion_cp)
    content = (data["choices"][0]['message']['content'])
    print(content)


question = '''
SW-AccountA-20250218A-SceneA-ModelA-S4SS1067/
├── 冰川白/
│   ├── 产品整体画面/
│   │   ├── 模特展示/
│   │   │   ├── 静态展示/
│   │   │   ├── 动态展示/
│   │   ├── 产品展示/
│   │   │   ├── 悬挂展示/
│   │   │   ├── 对比展示/
│   ├── 产品细节画面/
│   │   ├── 产品展示/
│   │   │   ├── 低领短帽檐/
│   │   │   ├── 立体宽松H裁剪/
│   │   │   ├── 后开马尾孔/
│   │   │   ├── 软帽檐/
│   │   │   ├── 加长勾手袖子/
│   │   │   ├── 两侧插袋/
│   │   │   ├── 下脚可调节扣/
│   │   ├── 模特展示/
│   │   │   ├── 低领短帽檐/
│   │   │   ├── 立体宽松H裁剪/
│   │   │   ├── 后开马尾孔/
│   │   │   ├── 软帽檐/
│   │   │   ├── 加长勾手袖子/
│   │   │   ├── 两侧插袋/
│   │   │   ├── 下脚可调节扣/
│   ├── 产品体验画面/
│   │   ├── 冰感/
│   │   ├── 清凉/
│   │   ├── 柔软/
│   │   ├── 舒适/
│   ├── 产品功能画面/
│   │   ├── 防晒/
│   │   ├── 阻隔紫外线/
│   │   ├── 吸湿速干/
│   │   ├── 透气/
│   │   ├── 藏肉显瘦/
│   ├── 产品风格画面/
│   │   ├── 简约风/
│   ├── 产品搭配画面/
│   │   ├── 休闲裤/        
│   │   ├── 微喇裤
│   │   ├── 超A小短裙
│   │   ├── 工装裤
│   ├── 产品运动场景画面/
│   │   ├── 户外/
│   │   ├── 跑步/
│   │   ├── 休闲日常/
│   │   ├── 网球/
│   │   ├── 骑行/

'''

chat_request(question)