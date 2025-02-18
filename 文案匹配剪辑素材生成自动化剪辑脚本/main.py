import os
from sw_package.file_read import xlsx_to_json
from config import pre_config
if __name__ =='__main__':

    # E 背景音乐dir
    bgmPath = r"\\xiawei\1号储存盘\SW速惟项目\服装信息流批量化模版\BGM"
    bgmOption = ["轻缓", "欢快", "动感", "热点快节奏"]  # input3 和根目录拼接

    # 用户配音选项
    dubbingSelection =["AI配音", "真人配音"]
    dobbingAI = ["紫薇"]    # input4


    # 拍摄行动规划
    shootingSchedule = "SW-AccountD-20250208A-SceneA-ModelA-S4AW4181-铁锈红"  # // input1

    # 视频模版选择  // input2
    videoTemplate = ["VT101", "VT102","VT103"]

    # 获取原始数据
    json_data = xlsx_to_json('inputData.xlsx')

    print(json_data[0])

    print(pre_config.bgm_option)


    data ={
    "视频编号": "",  # 数据序号
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