# 文件名：config.py
import os 
class ProjectConfig:
    def __init__(self):
        # 素材根目录

        self.root = r"\\xiawei\1号储存盘\SW速惟项目\视频素材库\SW"
        # 背景音乐路径
        self.bgm_path = r"\\xiawei\1号储存盘\SW速惟项目\服装信息流批量化模版\BGM"
        # 背景音乐选项
        self.bgm_option = ["轻缓", "欢快", "动感", "热点快节奏"]
        
        # 用户配音选项
        self.dubbing_selection = ["AI配音", "真人配音"]
        # AI配音选项
        self.dubbing_ai = ["TVB女声"]
        
        # 拍摄行动规划
        self.shooting_schedule = "SW-AccountA-20250220A-SceneA-ModelA-S4SS1067-冰川灰"
        
        # 视频模版选择
        self.video_template = ["VT101", "VT102", "VT103"]

        self.data =   {
        "视频编号": "",  # 数据序号
        "回溯信息": "",  # input1 + 文案模版号 + input2 + 时间 + 数据序号
        "视频名称": "",  # input1 + 文案模版号 + input2 + 时间 + 数据序号
        "视频字幕": "",  # 文案长度处理，分段按标点符号:, 。 ！ 每一段的长度然后分段 
        "切割数组": "",  # 同视频字幕
        "混剪素材": "",  # 发送文案至api 处理：截取 | 后面的内容
        "背景音乐": "",  # input3
        "配音文案": "",  # 输入文案内容
        "AI配音": "",   #  input4
        "配音文件路径": "",   # input5
        "音频分段命名": ""    # input6
        }



pre_config = ProjectConfig()

tempt_data = pre_config