import sys
from colorama import init, Fore, Back, Style

print(Fore.BLUE + "_"*30)
print("         >>星座查询<<       ")
print("       仅提供太阳星座查询")
print("_"*30)
print(Style.RESET_ALL)


def content():       # 主体部分

    def choose_one():
        choose = int(input(Fore.GREEN + "\t是否继续查询星座？1/0"))
        print(Style.RESET_ALL)
        print(choose)
        if choose == 1:
            content()
        elif choose == 0:
            sys.exit()
        else:
            print(Fore.RED + "未按照规则输入选择，可以使用 ‘0’ 直接退出进程")
            print(Style.RESET_ALL)
            choose_one()

    print("输入格式：10月24---> xxxx")
    birthday = input(Fore.GREEN + "输入-->生日:")
    print(Style.RESET_ALL)

    if len(birthday) == 4:  # 判断生日是四位的情况
        print("月份：", birthday[0:2], "日期：", birthday[2:], "准确无误")
        month = int(birthday[0:2])
        day = int(birthday[2:])

        if 0 < month <= 12 and 0 < day <= 32:
            if month == 10:
                if day <= 23:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：天枰座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：天蝎座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
            if month == 11:
                if day <= 22:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：天蝎座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：射手座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
            if month == 12:
                if day <= 21:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：射手座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：魔羯座")
                    print('=' * 30)
                    print(Style.RESET_ALL)

        else:
            print(Fore.RED + "输入的日期格式有误")
            print("未按照提示标准输入")
            print(Style.RESET_ALL)

    elif len(birthday) == 3 or 2:  # 判断生日是三位或者两位的情况
        print("月份：", birthday[0:1], "日期：", birthday[1:], "准确无误")
        month = int(birthday[0:1])
        day = int(birthday[1:])

        if 0 < month <= 12 and 0 < day <= 32:
            if month == 1:
                if day <= 19:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：魔羯座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：水瓶座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
            if month == 2:
                if day <= 18:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：水瓶座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：双鱼座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
            if month == 3:
                if day <= 20:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：双鱼座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：白羊座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
            if month == 4:
                if day <= 19:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：白羊座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：金牛座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
            if month == 5:
                if day <= 20:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：金牛座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：双子座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
            if month == 6:
                if day <= 21:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：双子座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：巨蟹座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
            if month == 7:
                if day <= 22:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：巨蟹座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：狮子座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
            if month == 8:
                if day <= 22:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：狮子座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：处女座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
            if month == 9:
                if day <= 22:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：处女座")
                    print('=' * 30)
                    print(Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + '=' * 30)
                    print("你的星座属性是：天枰座")
                    print('=' * 30)
                    print(Style.RESET_ALL)

        else:
            print(Fore.RED + "输入的日期格式有误")
            print("未按照提示标准输入")
            print(Style.RESET_ALL)

    def choose_one():
        choose = int(input(Fore.GREEN + "\t是否继续查询星座？1/0"))
        print(Style.RESET_ALL)
        print(choose)
        if choose == 1:
            content()
        elif choose == 0:
            sys.exit()
        else:
            print(Fore.RED + "未按照规则输入选择，可以使用 ‘0’ 直接退出进程")
            print(Style.RESET_ALL)
            choose_one()
    choose_one()


content()








