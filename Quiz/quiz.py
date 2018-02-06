import random
import numpy as np
import codecs
import time
import datetime
#https://gist.github.com/cwil323/9b1bfd25523f75d361879adfed550be2

def display_intro():
    title = "************* 复习小帮手 *************"
    print("*" * 2 * (len(title)-14))
    print(title)
    print("*" * 2 * (len(title)-14))
    print("(^し^)，准备好了吗？——挑战开始喽！")

def display_menu():
    menu_list = ["1. 小数加法", 
                "2. 小数减法", 
                "3. 二位乘法", 
                "4. 二位除法", 
                "5. 判断闰年", 
                "6. 算算日期", 
                "7. 听写单词", 
                "8. 休息休息"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])
    print(menu_list[3])
    print(menu_list[4])
    print(menu_list[5])
    print(menu_list[6])
    print(menu_list[7])

def display_separator():
    print("-^-" * 12)


def get_user_input():
    print("-^-" * 12)
    user_input = int(input("你想做什么题: "))
    while user_input > 8 or user_input <= 0:
        print("无效选项！")
        user_input = int(input("再试一次: "))
    else:
        return user_input


def get_user_solution(problem, total):
    print("第", total, "题")
    print(problem, end="")
    result = str(input(" = "))
    return result


def check_solution(user_solution, solution, count):
    if user_solution == solution:
        count = count + 1
        print("√！(*^▽^*)")
        return count
    else:
        print("×！(－＂－怒), 正确答案是：", solution)
        return count


def menu_option(index, count, total):
    if index is 1:
        number_one = random.randrange(10, 99) + round(random.random(), 2)
        number_two = random.randrange(10, 99) + round(random.random(), 2)
        problem = str(number_one) + " + " + str(number_two)
        solution = str(round(number_one + number_two, 2))
        user_solution = get_user_solution(problem, total)
        count = check_solution(user_solution, solution, count)
        return count
    elif index is 2:
        number_one = random.randrange(10, 99) + round(random.random(), 2)
        number_two = random.randrange(10, 99) + round(random.random(), 2)
        number_three = round(number_one + number_two, 2)
        problem = str(number_three) + " - " + str(number_two)
        solution = str(number_one)
        user_solution = get_user_solution(problem, total)
        count = check_solution(user_solution, solution, count)
        return count
    elif index is 3:
        number_one = random.randrange(10, 99)
        number_two = random.randrange(10, 99)
        problem = str(number_one) + " × " + str(number_two)
        solution = str(number_one * number_two)
        user_solution = get_user_solution(problem, total)
        count = check_solution(user_solution, solution, count)
        return count
    elif index is 4:
        number_one = random.randrange(10, 99)
        number_two = random.randrange(10, 99)
        number_three = number_one * number_two
        problem = str(number_three) + " ÷ " + str(number_two)
        solution = str(number_one)
        user_solution = get_user_solution(problem, total)
        count = check_solution(user_solution, solution, count)
        return count        
    elif index is 5:
        year = random.randrange(1, 9999)
        problem = str(year) + "是（0:平年，1:闰年）: "
        if year %400 == 0 :
            solution = 1
        elif year %4 == 0 :
            solution = 1
        else :
            solution = 0
        solution = str(solution)
        user_solution = get_user_solution(problem, total)
        count = check_solution(user_solution, solution, count)
        return count
    elif index is 6:
        a1=(2018,1,1,0,0,0,0,0,0)              #设置开始日期时间元组（1976-01-01 00：00：00）
        a2=(2018,12,31,23,59,59,0,0,0)    #设置结束日期时间元组（1990-12-31 23：59：59）
        start=time.mktime(a1)    #生成开始时间戳
        end=time.mktime(a2)      #生成结束时间戳
        date1 = datetime.date(*time.localtime(random.randint(start, end))[0:3])     #生成随机时间并转换为datetime日期对象
        date2 = datetime.date(*time.localtime(random.randint(start, end))[0:3])
        problem = str(date1) + " 和 " + str(date2) + " 之间差多少天？"
        solution = str(abs((date1 - date2).days))
        user_solution = get_user_solution(problem, total)
        count = check_solution(user_solution, solution, count)
        return count
    else:
        my_dict = {}
        with codecs.open("english.txt", mode = 'r', encoding = 'UTF-8') as f:
            for line in f:
                line=line.strip('\r\n')
                (key, val) = line.split(",")
                my_dict[key] = val
        keys = list(my_dict.keys())
        number_one = random.randrange(0, len(keys))
        problem = keys[number_one]
        solution = my_dict[keys[number_one]]
        user_solution = get_user_solution(problem, total)
        count = check_solution(user_solution, solution, count)
        return count        
 
def display_result(total, correct):
    if total > 0:
        result = correct / total
        percentage = round((result * 100), 2)
    if total == 0:
        percentage = 0
    print("你回答了", total, "个问题，答对", correct, "个。")
    if percentage >= 90:
        print("得分：", percentage, "ヾ(@^▽^@)ノ ☆哎哟不错哦", sep = "")
    else:
        print("得分：", percentage, "(*゜Д゜)σ 凸←自爆按钮", sep = "")
    

def main():
    display_intro()
    display_menu()
    display_separator()

    option = get_user_input()
    total = 0
    correct = 0
    while option != 8:
        total = total + 1
        correct = menu_option(option, correct, total)
        option = get_user_input()

    display_separator()
    print("************* 成绩公布 *************")
    display_separator()
    display_result(total, correct)
    display_separator()
    
if __name__ == "__main__":
    main()



