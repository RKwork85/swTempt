import os
import re
import json 
import time
import random
import multiprocessing
from openai import OpenAI
from config import pre_config

from sw_package.file_read import data_json, xlsx_to_json, create_output_folder
from sw_package.get_todayTime import todayTime
from sw_package.touchFile import touch_folder_files_dictFile



def datasolve(question_json):
    contentDealJons = split_sentences(question_json["文案内容"])
    videoSegmentNum = len(contentDealJons.commasCountList)
    videoSegmentStr = videoSegmentSolve(videoSegmentNum)

    # 匹配内容
    content = (data["choices"][0]['message']['content'])


    tempt_data = pre_config.data
    tempt_data["视频编号"] = todayTime() +"-" + question_json["ID"]
    tempt_data["回溯信息"] = pre_config.shooting_schedule + "-" + question_json["模板编号"] + "-" + random_choice(pre_config.video_template) + "-"+ todayTime() +"-" + question_json["ID"]
    tempt_data["视频名称"] = question_json["模板编号"] + "-" + random_choice(pre_config.video_template) + "-"+ todayTime() +"-" + question_json["ID"]
    tempt_data["视频字幕"] = contentDealJons.substringsStr
    tempt_data["切割数组"] = contentDealJons.commasCountStr
    
    concat = content_solved(content)


    tempt_data["混剪素材"] = concat
    tempt_data["背景音乐"] = pre_config.bgm_path + "\\" + random_choice(pre_config.bgm_option)
    tempt_data["配音文案"] = question_json["文案内容"]
    tempt_data["AI配音"] = random_choice(pre_config.dubbing_ai)
    print("最终返回：", tempt_data)
    return tempt_data

    
    # 会有死锁问题
    # pre_config.data["混剪素材"] = content_solved(content)
    
def videoSegmentSolve(segmentNumber):
    # 全局变量：所有的文件名
    random.sample(fileList, segmentNumber)
    
    return 



    pass
def task_running(task):
    file_list = []
    with multiprocessing.Pool(processes=100) as pool:
        results = pool.map_async(datasolve, task)
        for index,result in enumerate(results.get()):
            file_list.append(result)

    return file_list



def content_solved(content):
    lines = content.strip().split("\n")
    result = [line.split("|", 1)[1].strip() for line in lines]
    video_materials_data = data_json(f"output/{pre_config.shooting_schedule}.json")
    final_match = []
    for i in result:
        vdieo_materials_match = random_choice(video_materials_data[i])
        cat_data = pre_config.root + "/" +  pre_config.shooting_schedule +  "/" + i + "/" + vdieo_materials_match 
        final_match.append(cat_data)
    final_match_str = "\n".join(final_match)

    # 需要将所有的斜杠改为反斜杠
    final_match_str_solved = final_match_str.replace("/", "\\")

    return final_match_str_solved


def random_choice(lst):
    if not lst:  
        return ""
    return random.choice(lst)


def split_sentences(text):
    # 使用“。”和“！”作为分隔符分割文本
    sentences = []
    temp_sentence = ""
    for char in text:
        temp_sentence += char
        if char in "。！？":  
            sentences.append(temp_sentence.strip())
            temp_sentence = ""  
    if temp_sentence.strip():  # 如果最后还有未处理的文本且不为空
        sentences.append(temp_sentence.strip())  # 去除空白字符后添加

    # 调用函数统计标点符号数量和切割子串
    commasCountList, substringsList = count_commas_plus_one(sentences)

    # 将结果转换为字符串形式
    sentencesStr = "\n".join(sentences)
    commasCountStr = "\n".join(commasCountList)
    substringsStr = "\n".join(substringsList)

    return {"sentencesStr":sentencesStr,"commasCountStr" :commasCountStr, "substringsStr":substringsStr,"sentences":sentences,"commasCountList":commasCountList,"substringsList":substringsList  }


def count_commas_plus_one(sentences):
    result = []
    all_substrings = []
    # 遍历输入的句子列表
    for sentence in sentences:
        # 统计当前句子中逗号、顿号和分号的数量
        comma_count = sentence.count('，')  # 中文逗号
        pause_mark_count = sentence.count('、')  # 顿号
        semicolon_count = sentence.count(';')  # 分号
        # 将所有标点数量加 1后存入结果列表
        result.append(str(comma_count + pause_mark_count + semicolon_count + 1))
        
        # 替换顿号和分号为逗号，以便统一使用逗号进行切割
        modified_sentence = sentence.replace('、', '，').replace(';', '，')
        # 使用逗号进行切割
        substrings = modified_sentence.split('，')
        
        # 使用正则表达式去除每个子串中的标点符号
        cleaned_substrings = [re.sub(r'[，。；！]', '', sub) for sub in substrings]
        
        # 将清理后的子串添加到总列表中
        all_substrings.extend(cleaned_substrings)
    
    return result, all_substrings


if __name__ =='__main__':

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    touch_folder_files_dictFile(os.path.join(pre_config.root,pre_config.shooting_schedule))

    input_data = xlsx_to_json('inputData.xlsx')
    
    file_list = []
    samples =input_data[:30]
    start = time.time()

    result_file = datasolve(samples)
    end = time.time()
    print(f"最终执行时间{end - start}")
    
    with open("final_result.json", "w", encoding="utf-8") as f:
        json.dump(result_file, f, indent=4, ensure_ascii=False)




