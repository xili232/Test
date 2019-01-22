# 学生信息管理系统
from menu import show_menu
from student_info import *

def main():
    L = []
    while True:
        show_menu()
        _input = input('请输入命令')
        if _input == 'q':    # 退出
            break
        elif _input == '1':
            input_student(L)
        elif _input == '2':
            print_student(L)
        elif _input == '3':
            del_student(L)
        elif _input == '4':
            mod_student(L)
        elif _input == '5':
            score_h(L)
        elif _input == '6':
            score_l(L)
        elif _input == '7':
            age_h(L)
        elif _input == '8':
            age_l(L)
        elif _input == '9':
            L = read_from_file()
        elif _input == '10':
            save_to_file(L)
        else:
            print('命令输入错误')
    
main()