#  将文案2 批量导入数据库


import pymysql

def insert_data_from_file(file_path):
    """
    从文本文件中读取数据并插入到MySQL数据库的Area_Marketing表中。

    参数:
        file_path (str): 文本文件的路径
    """
    # 连接到MySQL数据库
    connection = pymysql.connect(
        host='192.3.211.151',  # 替换为您的 MySQL 服务器地址
        user='root',  # 替换为您的用户名
        password='123456',  # 替换为您的密码
        database='FZDB',  # 使用 FZDB 数据库
        charset='utf8mb4',
        port=3307,
        autocommit=True
    )

    try:
        # 创建游标对象
        cursor = connection.cursor()

        # 打开文本文件并按行读取
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 初始化ID
        id = 1

        # 遍历每一行内容并插入数据库
        for line in lines:
            # 去除行首行尾的空白字符
            template_content = line.strip()

            # 构造Template_Name
            template_name = f"Bb    {id}"

            # 插入数据的SQL语句
            insert_sql = """
            INSERT INTO Welfare_Marketing (ID, Template, Template_Class, Template_Name)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_sql, (id, template_content, "福利营销", template_name))

            # 自增ID
            id += 1

        print(f"数据插入完成，共插入 {id - 1} 条记录。")

    except Exception as e:
        print(f"发生错误：{e}")
    finally:
        # 关闭数据库连接
        connection.close()

# 调用函数，传入文本文件路径
file_path = "/home/rkwork/rkwork/project/swTemp-main/文案内容/文案2.txt"  # 替换为你的文本文件路径
insert_data_from_file(file_path)