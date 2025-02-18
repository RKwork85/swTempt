import pymysql

def add_template_name_field():
    # 数据库连接
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

        # Step 1: 添加新字段 Template_Name
        alter_sql = """
        ALTER TABLE Daily_Topics
        ADD COLUMN Template_Name VARCHAR(255);
        """
        cursor.execute(alter_sql)
        print("字段 Template_Name 已成功添加到表 Personality_Topics。")

        # Step 2: 更新 Template_Name 字段的值为 'Ca' + ID
        update_sql = """
        UPDATE Daily_Topics
        SET Template_Name = CONCAT('Ca', ID);
        """
        cursor.execute(update_sql)
        print(f"字段 Template_Name 已成功更新，共更新 {cursor.rowcount} 条记录。")

    except Exception as e:
        print(f"发生错误：{e}")
    finally:
        # 关闭数据库连接
        connection.close()

# 调用函数
add_template_name_field()