import sys

def start():

    id_num = input("ID number:")
    now_year = int(input("now year:"))
    now_year_end = now_year - 150
    # 4  2|  9  0  0  6  |2  0  0  1|   1  0|  2  4|  1  2  1  3     18位二代身份证
    # 0  1|  2  3  4  5  |6  7  8  9|  10 11| 12 13| 14 15 16 17
    if len(id_num) == 18:
        print("--｜To verify")
        print("-" * 32)

        birth_year = int(id_num[6:10])
        birth_month = int(id_num[10:12])
        birth_day = int(id_num[12:14])
        print("eight-digit birth date code:", birth_year, birth_month, birth_day)
        if now_year_end <= birth_year <= now_year:
            print("birth year pass-test\nThe age of the id card holder is:", 2022 - birth_year + 1)
            if 1 <= birth_month <= 12:
                if 1 <= birth_day <= 32:
                    print("birthday pass-test\nThe birthday of the id card holder is:", birth_month, birth_day)
                else:
                    print("error:day input error")
                    sys.exit()
            else:
                print("error:month input error")
                sys.exit()
        else:
            print("error:year input error")
            sys.exit()

        print("-"*32)
        address_1 = int(id_num[0:2])
        address_2 = int(id_num[2:6])
        print("six-digit address code:", address_1, address_2)
        if 11 <= address_1 <= 15:
            print("address pass-test\n-->", "京、津、冀、晋、蒙")
        elif 21 <= address_1 <= 23:
            print("address pass-test\n-->", " 辽、吉、黑 ")
        elif 31 <= address_1 <= 37:
            print("address pass-test\n-->", "沪、苏、浙、皖、闽、赣、鲁")
        elif 41 <= address_1 <= 46:
            print("address pass-test\n-->", "豫、鄂、湘、粤、桂、琼")
        elif 50 <= address_1 <= 54:
            print("address pass-test\n-->", "渝、川、贵、云、藏")
        elif 61 <= address_1 <= 65:
            print("address pass-test\n-->", "陕、甘、青、宁、新")
        else:
            print("error:address input error")
            sys.exit()

        print("-"*32)
        gender = int(id_num[16])
        if gender%2 == 0:
            print("gender pass-test\n--> 女")
        else:
            print("gender pass-test\n--> 男")

    else:
        print("error:The length of the ID is incorrect")
        sys.exit()


start()
