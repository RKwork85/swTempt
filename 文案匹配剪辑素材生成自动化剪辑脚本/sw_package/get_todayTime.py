from datetime import datetime


def todayTime():
    # 获取当前日期
    today = datetime.today()

    # 格式化日期为 YYYYMMDD 格式
    formatted_date = today.strftime("%Y%m%d")
    return formatted_date

