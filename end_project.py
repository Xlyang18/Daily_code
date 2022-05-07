import os
import jieba
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox

list_student = []
test_list = []


class Stats:
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(200, 200)
        self.window.move(300, 300)
        self.window.setWindowTitle('自动化校验作业')

        self.button1 = QPushButton('校验', self.window)
        self.button1.move(50, 80)

        self.button1.clicked.connect(self.content_data)

    def content_data(self=None):
        # 此处地址为：存放搜集到的学生作业文件夹地址
        path = "/Users/xiongluyang/Documents/New_FullProject/自动化校验作业/content"
        datanames = os.listdir(path)
        for i in datanames:
            list_student.append(i)
        print("已收到的作业有：")
        print(list_student)
        new_data = str(list_student)
        print("分词后的结果：")
        # print("/".join(jieba.lcut(new_data, cut_all=True)))  # 备选分词方案
        new_data_jieba = jieba.lcut_for_search(new_data)
        # print("/".join(jieba.lcut_for_search(new_data)))  # 测试语句（校验查词功能是否正常）
        print(new_data_jieba)

        # 此处为同级目录下的.txt文件（用于存放学生姓名）
        # .txt内存放数据的格式为：    ["熊路阳","张三","李四","王五"]
        if os.path.exists("目标.txt"):
            f = open("目标.txt", 'r', encoding='utf-8')
            ret = f.read()
            test_list = eval(ret)
            # 关闭文件
            f.close()

        print(test_list)

        for i in test_list:
            for j in new_data_jieba:
                if i == j:
                    test_list.remove(i)

        print(test_list)
        QMessageBox.about(self.window, '校验结果',
                          f'''未交作业的名单{test_list}''')


app = QApplication([])
stats = Stats()
stats.window.show()
app.exec_()
