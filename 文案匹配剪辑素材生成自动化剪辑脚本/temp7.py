import re

def split_sentences(text):
    # 使用“。”和“！”作为分隔符分割文本
    sentences = []
    temp_sentence = ""
    for char in text:
        temp_sentence += char
        if char in "。！":  
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

    return sentencesStr, commasCountStr, substringsStr


def count_commas_plus_one(sentences):
    # 创建一个空列表用于存储结果
    result = []
    # 创建一个空列表用于存储所有句子切割后的子串
    all_substrings = []
    # 遍历输入的句子列表
    for sentence in sentences:
        # 统计当前句子中逗号、顿号和分号的数量
        comma_count = sentence.count('，')  # 中文逗号
        pause_mark_count = sentence.count('、')  # 顿号
        semicolon_count = sentence.count(';')  # 分号
        # 将所有标点数量加 1后存入结果列表
        result.append(str(comma_count + pause_mark_count + semicolon_count + 1))
        
        # 按照逗号、顿号和分号进行切割
        # 替换顿号和分号为逗号，以便统一使用逗号进行切割
        modified_sentence = sentence.replace('、', '，').replace(';', '，')
        # 使用逗号进行切割
        substrings = modified_sentence.split('，')
        
        # 使用正则表达式去除每个子串中的标点符号
        cleaned_substrings = [re.sub(r'[，。；！]', '', sub) for sub in substrings]
        
        # 将清理后的子串添加到总列表中
        all_substrings.extend(cleaned_substrings)
    
    return result, all_substrings


# 输入文本
text = "速惟羊毛开衫，真的绝！100%绵羊毛，温暖呵护。法式慵懒设计，尽显随性魅力。优雅小圆领，展露迷人锁骨。日常休闲必备，赶紧冲！"
# 调用函数
question, commasCountStr, substringsStr = split_sentences(text)

# 输出结果
print("分割后的句子：")
print(question)
print("标点符号数量加 1的结果：")
print(commasCountStr)
print("所有句子切割后的子串：")
print(substringsStr)