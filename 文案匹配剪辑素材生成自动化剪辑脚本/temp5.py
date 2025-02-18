import re
def process_data(text):
    # 存储每条数据长度处理结果的数组
    data_list = [item.strip() for item in re.split(r'[。！]+', text) if item.strip()]
    length_results = []
    # 存储处理后的新字符串数组
    new_strings = []

    for data in data_list:
        # 计算字符长度处理结果
        length_result = (len(data) // 10) + 1
        length_results.append(length_result)

        # 根据字符长度进行不同处理
        if len(data) <= 10:
            # 字符长度小于等于10，不做处理
            new_strings.append(data)
        elif 10 < len(data) < 15:
            # 字符长度大于10且小于15，截断为两个字符串
            split_index = (len(data) // 2) + 2
            new_strings.append(data[:split_index])
            new_strings.append(data[split_index:])
        elif 15 <= len(data) < 20:
            # 字符长度大于等于15且小于20，截断为两个字符串
            split_index = (len(data) // 2)  +1
            new_strings.append(data[:split_index])
            new_strings.append(data[split_index:])
        else:
            # 字符长度大于等于20，始终保持截断后的每个子串最小长度为4
            split_index = 7
            while len(data) > 0:
                new_strings.append(data[:split_index])
                data = data[split_index:]

    return length_results, new_strings

# 示例数据
data_list = "终于把速惟的羊毛开衫价格打下来了！100%绵羊毛，柔软亲肤，温暖舒适。小圆领露锁骨，显魅力。宽松版型，随性自在，赶紧冲！"
# 处理数据
length_results, new_strings = process_data(data_list)

# 输出结果
print("长度处理结果数组：", length_results)
print("新的字符串数组：", new_strings)