import pymysql

def drop_column():
    # 数据库连接
    connection = pymysql.connect(
        host='192.3.211.151',
        user='root',
        password='123456',
        database='FZDB',
        charset='utf8mb4',
        port=3307,
        autocommit=True
    )

    try:
        # 创建游标对象
        cursor = connection.cursor()

        # 删除字段 Template_Name
        drop_sql = """
        ALTER TABLE Function_Topics
        DROP COLUMN Template_Name;
        """
        cursor.execute(drop_sql)
        print("字段 Template_Name 已成功从表 Function_Topics 中删除。")

    except Exception as e:
        print(f"发生错误：{e}")
    finally:
        # 关闭数据库连接
        connection.close()

# 调用函数
drop_column()