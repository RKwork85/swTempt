import os
import sys
import subprocess
from PyQt5 import QtWidgets, QtGui, QtCore

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class VideoTrimmerApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 修改应用名称和图标
        self.setWindowTitle('视频素材清理应用')
        self.setWindowIcon(QtGui.QIcon(resource_path('icons\\app-icon.png')))
        self.setMinimumSize(650, 600)
        self.setGeometry(100, 100, 400, 300)
        self.center()
        # 设置样式表
        self.setStyleSheet("""
            QWidget {
                font-size: 14px;
                background-color: #f5f5f5;
            }   
            QLineEdit {
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: #fff;
            }
            QLineEdit:focus {
                border: 1px solid #1e90ff;
                border-bottom-width: 2px;
            }
            QPushButton {
                padding: 10px;
                background-color: #1e90ff;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #1c86ee;
            }
            QLabel {
                margin-bottom: 5px;
            }
            QTextEdit {
                background-color: #fff;
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 10px;
                min-height: 100px;
            }
            QProgressBar {
                border: 1px solid #ddd;
                border-radius: 5px;
                text-align: center;
                background-color: #fff;
            }
            QProgressBar::chunk {
                background-color: #32cd32; 
                width: 20px;
            }
        """)

        # 输入文件夹路径
        self.input_folder_label = QtWidgets.QLabel('素材文件夹:')
        self.input_folder_edit = QtWidgets.QLineEdit(self)
        self.input_folder_button = QtWidgets.QPushButton('浏览文件夹', self)
        self.input_folder_button.setIcon(QtGui.QIcon(resource_path('icons\\folder-open.png')))
        self.input_folder_button.clicked.connect(self.browse_input_folder)

        # 输出文件夹路径
        self.output_folder_label = QtWidgets.QLabel('输出文件夹:')
        self.output_folder_edit = QtWidgets.QLineEdit(self)
        self.output_folder_button = QtWidgets.QPushButton('浏览文件夹', self)
        self.output_folder_button.setIcon(QtGui.QIcon(resource_path('icons\\folder-open.png')))
        self.output_folder_button.clicked.connect(self.browse_output_folder)

        # 去除前几秒
        self.trim_seconds_label = QtWidgets.QLabel('去除前几秒:')
        self.trim_seconds_edit = QtWidgets.QLineEdit(self)

        # 进度条和进度信息
        self.progress_bar = QtWidgets.QProgressBar(self)
        self.progress_label = QtWidgets.QLabel('进度: 0%', self)

        # 开始处理按钮
        self.process_button = QtWidgets.QPushButton('开始处理', self)
        self.process_button.setIcon(QtGui.QIcon(resource_path('icons\\play.png')))
        self.process_button.clicked.connect(self.trim_videos)

        # 处理状态显示
        self.status_label = QtWidgets.QLabel('输出日志:')
        self.status_display = QtWidgets.QTextEdit(self)
        self.status_display.setReadOnly(True)

        # 布局
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.input_folder_label)
        layout.addWidget(self.input_folder_edit)
        layout.addWidget(self.input_folder_button)
        layout.addSpacing(10)
        layout.addWidget(self.output_folder_label)
        layout.addWidget(self.output_folder_edit)
        layout.addWidget(self.output_folder_button)
        layout.addSpacing(10)
        layout.addWidget(self.trim_seconds_label)
        layout.addWidget(self.trim_seconds_edit)
        layout.addSpacing(20)
        layout.addWidget(self.process_button)
        layout.addSpacing(20)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.progress_label)
        layout.addSpacing(20)
        layout.addWidget(self.status_label)
        layout.addWidget(self.status_display)

        self.setLayout(layout)

    def browse_input_folder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, '选择素材文件夹目录')
        if folder:
            self.input_folder_edit.setText(folder)

    def browse_output_folder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, '选择输出文件夹目录')
        if folder:
            self.output_folder_edit.setText(folder)

    def trim_videos(self):
        input_folder = self.input_folder_edit.text()
        output_folder = self.output_folder_edit.text()
        trim_seconds = self.trim_seconds_edit.text()

        if not input_folder or not output_folder or not trim_seconds.isdigit():
            QtWidgets.QMessageBox.warning(self, '输入错误', '输入错误')
            return

        trim_seconds = int(trim_seconds)

        # 在输出文件夹路径中添加“处理后素材”子目录
        processed_folder = os.path.join(output_folder, "处理后素材")

        # 确保输出文件夹和“处理后素材”子目录存在
        if not os.path.exists(processed_folder):
            os.makedirs(processed_folder)

        # 获取输入文件夹中的所有文件
        files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
        total_files = len(files)

        if total_files == 0:
            QtWidgets.QMessageBox.information(self, '没有文件', '没有找到任何视频文件')
            return

        # 初始化进度条
        self.progress_bar.setMaximum(total_files)
        self.progress_bar.setValue(0)
        self.progress_label.setText('进度: 0%')

        # 清空状态显示
        self.status_display.clear()

        # 遍历输入文件夹中的所有文件
        for i, filename in enumerate(files):
            input_path = os.path.join(input_folder, filename)

            if os.path.isfile(input_path):
                output_path = os.path.join(processed_folder, filename)

                # 将秒数转换为 HH:MM:SS 格式
                hours = trim_seconds // 3600
                minutes = (trim_seconds % 3600) // 60
                seconds = trim_seconds % 60
                trim_time = f"{hours:02}:{minutes:02}:{seconds:02}"

                # 使用 FFmpeg 去除指定的秒数，并重新编码音频，同时保留元数据
                ffmpeg_path = resource_path(r'C:\Users\rkwor\Downloads\ffmpeg-7.1-essentials_build\bin\ffmpeg')
                command = [
                    ffmpeg_path, '-ss', trim_time, '-i', input_path, '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', 
                    '-map_metadata', '0', '-y', output_path
                ]

                # 执行命令
                try:
                    result = subprocess.run(command, check=True, stderr=subprocess.PIPE, text=True, encoding='utf-8',
                                            creationflags=subprocess.CREATE_NO_WINDOW)
                    self.status_display.append(f"Processed {filename} successfully.")
                except subprocess.CalledProcessError as e:
                    self.status_display.append(f"Error processing {filename}: {e.stderr}")

                # 更新进度条和进度信息
                self.progress_bar.setValue(i + 1)
                progress_percentage = int((i + 1) / total_files * 100)
                self.progress_label.setText(f'进度: {progress_percentage}%')

        QtWidgets.QMessageBox.information(self, '处理完毕', '所有视频处理完成')

    def center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2, (screen.height() - size.height() - 250) // 2)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = VideoTrimmerApp()
    window.show()
    sys.exit(app.exec_())

