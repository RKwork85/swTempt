import os
import subprocess
import openpyxl
from concurrent.futures import ThreadPoolExecutor

def get_video_info(file_path):
    """
    使用 ffprobe 获取视频文件的信息，包括时长和大小。
    """
    # 获取文件大小（字节）
    file_size_bytes = os.path.getsize(file_path)
    # 转换为 MB
    file_size_mb = file_size_bytes / (1024 * 1024)

    # 使用 ffprobe 获取视频时长
    command = [
        "ffprobe",
        "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        file_path
    ]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    duration = float(result.stdout) if result.returncode == 0 else None

    return file_path, duration, file_size_mb

def create_excel_report(folder_path, output_file):
    """
    创建一个 Excel 文件，记录视频文件的信息。
    """
    # 创建一个新的 Excel 工作簿
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Video Info"

    # 写入表头
    sheet.append(["Video Name", "Duration (seconds)", "Size (MB)"])

    # 获取所有视频文件路径
    video_files = [
        os.path.join(folder_path, filename)
        for filename in os.listdir(folder_path)
        if filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv', '.flv'))
    ]

    # 使用线程池并行处理视频文件
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_video_info, file_path) for file_path in video_files]
        for future in futures:
            file_path, duration, file_size_mb = future.result()
            filename = os.path.basename(file_path)
            # 将信息写入 Excel
            sheet.append([filename, duration, file_size_mb])
            # 打印视频信息
            print(f"Processed: {filename}, Duration: {duration:.2f} seconds, Size: {file_size_mb:.2f} MB")

    # 保存 Excel 文件
    workbook.save(output_file)
    print(f"Video information saved to {output_file}")

# 示例用法
input_folder = "/home/rkwork/rkwork/project/httpVenv/video"
output_file = "video_info.xlsx"

create_excel_report(input_folder, output_file)