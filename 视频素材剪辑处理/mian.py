import os
import subprocess

def trim_videos(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        
        if os.path.isfile(input_path):
            output_path = os.path.join(output_folder, filename)
            
            
            command = [
                r'ffmpeg', '-ss', '00:00:01', '-i', input_path, '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', 
                '-map_metadata', '0', '-y', output_path
            ]
            try:
                result = subprocess.run(command, check=True, stderr=subprocess.PIPE, text=True, encoding='utf-8')
                print(f"Processed {filename} successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Error processing {filename}: {e.stderr}")




input_folder = r"/home/rkwork/小蝶-海沫绿-1s"


output_folder = r"/home/rkwork/小蝶-海沫绿-output/"


# 执行批量处理
trim_videos(input_folder, output_folder)