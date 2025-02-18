import random
import json

def random_choice(lst):
    if not lst:  # 如果列表为空，返回 None 或抛出异常
        return None
    return random.choice(lst)

# 示例使用
my_list = [1, 2, 3, 4, 5]
random_element = random_choice(my_list)
print(f"随机选择的元素是: {random_element}")


with open("folder_files_dict.json", "r", encoding="utf-8") as f:
    materials_json = json.loads(f.read())
    # for i in f:
    #     print(i)


choice_data = random_choice(materials_json["铁锈红/产品搭配画面/蓝色牛仔裤"])
print(choice_data)