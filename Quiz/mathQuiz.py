import random
#https://gist.github.com/cwil323/9b1bfd25523f75d361879adfed550be2

def display_intro():
    title = "** 逗逗数学小测验 **"
    print("*" * len(title))
    print(title)
    print("*" * len(title))


def display_menu():
    menu_list = ["1. 加法", "2. 减法", "3. 乘法", "4. 除法", "5. 闰年", "6. 投降"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])
    print(menu_list[3])
    print(menu_list[4])
    print(menu_list[5])


def display_separator():
    print("-" * 24)


def get_user_input():
    user_input = int(input("选一个: "))
    while user_input > 6 or user_input <= 0:
        print("Invalid menu option.")
        user_input = int(input("Please try again: "))
    else:
        return user_input


def get_user_solution(problem, correct, total, percentage):
    score(total, correct, percentage)
    print("第", total, "题, 当前得分：", percentage)
    print(problem, end="")
    result = int(input(" = "))
    return result


def check_solution(user_solution, solution, count):
    if user_solution == solution:
        count = count + 1
        print("√！(*^▽^*)")
        return count
    else:
        print("×！(－＂－怒), 正确答案是：", solution)
        return count

def score(total, correct, percentage):
    if total > 0:
        result = correct / total
        percentage = round((result * 100), 2)
    if total == 0:
        percentage = 0
    return(total)
    return(correct)
    return(percentage)


def menu_option(index, correct, total, count, percentage):
    if index is 1:
        number_one = random.randrange(10, 999)
        number_two = random.randrange(10, 999)
        problem = str(number_one) + " + " + str(number_two)
        solution = number_one + number_two
        user_solution = get_user_solution(problem, correct, total, percentage)
        count = check_solution(user_solution, solution, count)
        return count
    elif index is 2:
        number_one = random.randrange(10, 999)
        number_two = random.randrange(10, 999)
        number_three = number_one + number_two
        problem = str(number_three) + " - " + str(number_two)
        solution = number_one
        user_solution = get_user_solution(problem, correct, total, percentage)
        count = check_solution(user_solution, solution, count)
        return count
    elif index is 3:
        number_one = random.randrange(10, 99)
        number_two = random.randrange(10, 99)
        problem = str(number_one) + " × " + str(number_two)
        solution = number_one * number_two
        user_solution = get_user_solution(problem, correct, total, percentage)
        count = check_solution(user_solution, solution, count)
        return count
    elif index is 4:
        number_one = random.randrange(10, 99)
        number_two = random.randrange(10, 99)
        number_three = number_one * number_two
        problem = str(number_three) + " ÷ " + str(number_two)
        solution = number_one
        user_solution = get_user_solution(problem, correct, total, percentage)
        count = check_solution(user_solution, solution, count)
        return count
    else:
        year = random.randrange(1, 9999)
        problem = str(year) + "是（0:平年，1:闰年）: "
        if year %400 == 0 :
            solution = 1
        elif year %4 == 0 :
            solution = 1
        else :
            solution = 0
        user_solution = get_user_solution(problem, correct, total, percentage)
        count = check_solution(user_solution, solution, count)
        return count

def display_result(total, correct, percentage):
    score(total, correct, percentage)
    print("你回答了", total, "个问题，答对了", correct, "个。")
    if percentage >= 90:
        print("你的得分是：", percentage, "分，(σﾟ∀ﾟ)σ..:*☆哎哟不错哦", sep = "")
    else:
        print("你的得分是：", percentage, "分，（*゜Д゜）σ凸←自爆按钮", sep = "")
    

def main():
    display_intro()
    display_menu()
    display_separator()

    option = get_user_input()
    total = 0
    correct = 0
    percentage = 0
    while option != 6:
        total = total + 1
        correct = menu_option(option, correct, total, count, percentage)
        option = get_user_input()

    print("Exit the quiz.")
    display_separator()
    display_result(total, correct, percentage)

main()

if __name__ == "__main__":
    main()



