import time

'''
time_left = 5
while time_left > 0:
    print("倒计时（s）", time_left)
    time.sleep(3)
    time_left = time_left - 1
'''


def level_1():
    print('\t', '_' * 30)
    print("\t  [--->->>倒计时整合系统<<-<---]    ")
    print('\t', '-' * 30)
    print('\t', '=' * 30)
    print("\t  [倒计时10(s)]<--------------")
    print("\t  [倒计时60(s)]<--------------")
    print("\t  [倒计时20(m)]<--------------")
    print("\t  [倒计时25(m)]<--------------")
    print("\t  [自定义xx(s/m)]<------------")
    print('\t', '=' * 30)
    choose = input("\t 选择此时你需要的[倒计时]-->")
    print(time.time())  # 时间戳
    print(time.ctime())  # 人类可视化时间戳
    if choose == '10':
        d10()
    elif choose == '60':
        d60()
    elif choose == '20':
        d20()
    elif choose == '25':
        d25()
    elif choose == 'xx' or 'XX':
        customization()


def d10():
    print("[倒计时10(s)]<--------------")
    time_left = 10
    while time_left > 0:
        print("倒计时（s）", time_left)
        time.sleep(1)
        time_left = time_left - 1


def d60():
    print("[倒计时60(s)]<--------------")
    time_left = 60
    while time_left > 0:
        print("倒计时（s）", time_left)
        time.sleep(1)
        time_left = time_left - 1


def d20():
    print("[倒计时20(m)]<--------------")
    time_left = 20
    while time_left > 0:
        print("倒计时（m）", time_left)
        time.sleep(60)
        time_left = time_left - 1


def d25():
    print("[倒计时25(m)]<--------------")
    time_left = 25
    while time_left > 0:
        print("倒计时（m）", time_left)
        time.sleep(60)
        time_left = time_left - 1


def customization():
    time_go = input("输入带有单位的时间值：")
    print("[倒计时", time_go[:-1], '(', time_go[-1], ')]<--------------')
    time_gg = int(time_go[:-1])
    if time_go[-1] == 's' or 'S':
        while time_gg > 0:
            print("倒计时（s）", time_gg)
            time.sleep(1)
            time_gg = time_gg - 1
    elif time_go[-1] == 'm' or 'M':
        while time_gg > 0:
            print("倒计时（m）", time_gg)
            time.sleep(60)
            time_gg = time_gg - 1
    else:
        print('!!!')


level_1()
from playsound import playsound

playsound('over.mp3')
