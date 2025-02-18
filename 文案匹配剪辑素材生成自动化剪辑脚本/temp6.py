def split_sentences(text):
    # 使用“。”和“！”作为分隔符分割文本
    sentences = []
    temp_sentence = ""
    for char in text:
        temp_sentence += char
        if char in "。！":  # 检查是否是句子结束符
            # 去除句子首尾的空白字符后存入列表
            sentences.append(temp_sentence.strip())
            temp_sentence = ""  # 重置临时句子变量
    if temp_sentence.strip():  # 如果最后还有未处理的文本且不为空
        sentences.append(temp_sentence.strip())  # 去除空白字符后添加
    return sentences

# 示例输入
text = "活着活着，你就会明白，人要学会改变自己，不要试图改变别人。改变自己是神，改变别人是神经病。成年人的世界，要学会筛选，而不是教育。人生有三把钥匙，接受、改变、放下。接受不了就改变，改变不了就放下。生活皆是成长，成长便是人生。轻轻的放下焦虑，暖暖的拥抱自己。若已经竭尽全力，那就顺其自然。"
result = split_sentences(text)
print(result)
print(len(result[2]))


def count_commas_plus_one(sentences):
    # 创建一个空列表用于存储结果
    result = []
    # 遍历输入的句子列表
    for sentence in sentences:
        # 统计当前句子中逗号、顿号和分号的数量
        comma_count = sentence.count('，')  # 中文逗号
        pause_mark_count = sentence.count('、')  # 顿号
        semicolon_count = sentence.count(';')  # 分号
        # 将所有标点数量加1后存入结果列表
        result.append(comma_count + pause_mark_count + semicolon_count + 1)
    return result

# 示例输入数组
sentences = result
# 调用函数并打印结果
result = count_commas_plus_one(sentences)
print(result)