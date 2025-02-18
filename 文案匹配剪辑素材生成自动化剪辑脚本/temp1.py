# 示例字符串
text = """
这件真不贵啦 | 铁锈红/产品整体画面/模特展示/动态展示/S&W1a2b3c4d.mp4  
花普通开衫的钱买到100%绵羊毛的 | 铁锈红/产品体验画面/亲肤柔软/S&W5e6f7g8h.mp4  
还是宽松版型，自在舒适 | 铁锈红/产品风格画面/慵懒风/S&W3m4n5o6p.mp4  
特别是小圆领设计，太显锁骨啦 | 铁锈红/产品细节画面/产品展示/优雅小圆领/S&W1u2v3w4x.mp4  
日常休闲穿都很合适 | 铁锈红/产品整体画面/模特展示/动态展示/S&W9c0d1e2f.mp4  
"""

# 按行分割字符串
lines = text.strip().split("\n")

# 截取 | 后的内容
result = [line.split("|", 1)[1].strip() for line in lines]

# print(result)
# # 输出结果
# for item in result:
#     print(item)

result = "\n".join([line.split("|", 1)[1].strip() for line in lines])
print(result)