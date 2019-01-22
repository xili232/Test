from student import Student 

def _menu(x):
    def _show(l):
        x(l)
        input('按回车继续')
    return _show

def input_student(l):    # 添加学生信息
    while True:
        name = input('请输入学生姓名[回车停止输入]')
        if not name:
            return l
        while True:
            try:
                age = int(input('请输入学生年龄'))
                if age <= 0:
                    print('年龄小于0, 请重新输入')
                    continue
                break
            except:
                print('年龄格式错误')
                continue
        while True:
            try:
                score = int(input('请输入学生分数'))
                if not (0 <= score <= 100):
                    print('分数超出范围(0~100), 请重新输入')
                break
            except:
                print('分数格式错误')
                continue
        l.append(Student(name, age, score))

@_menu
def print_student(l):    # 显示学生信息
    print(l)
    def num_chi(x):    # 判断中文字符个数
        m = 0
        for i in x:
            if 0x4e00<=ord(i)<=0x9fbf:
                m += 1
        return m
    print('+------------------+-------------+-------------+')
    print('|       name       |     age     |    score    |')
    print('+------------------+-------------+-------------+')
    for x in l:
        n, a, s = x.get_infos_string()
        print('|'+n.center(18-num_chi(n))+
              '|'+a.center(13)+
              '|'+s.center(13)+'|')
    print('+------------------+-------------+-------------+')

def del_student(l):    # 删除学生信息
    _name = input('请输入要删除的学生姓名')
    for x in l:
        if x.get_name() == _name:
            print('姓名:',x.get_name(),'年龄:',x.get_age(),'成绩:',x.get_score())
            i = int(input('是否删除该学生信息 [1]是, [2]否:'))
            if i == 1:
                l.remove(x)
                print('已删除')
                return
            elif i == 2:    # 重名则跳到下一个
                continue
            else:
                print('命令输入错误')
                return
    else:
        print('未找到'+_name) 

def mod_student(l):    # 修改学生信息
    _name = input('请输入要修改信息的学生姓名')
    for x in l:
        if x.get_name() == _name:
            print('姓名:',x.get_name(),
                  '年龄:',x.get_age(),
                  '成绩:',x.get_score())
            try:
                i = int(input('是否修改该学生信息 [1]是, [2]否:'))
            except: 
                print('命令输入错误')
                return
            if i == 1:
                n = input('重新输入姓名, 默认请按回车')
                x.name = n if n else _name
                while True:
                    try:
                        x.age = int(input('重新输入年龄'))
                        if x.age <= 0:
                            print('年龄小于0, 请重新输入')
                            continue
                        break
                    except:
                        print('年龄输入错误, 请重新输入')
                        continue
                while True:
                    try:
                        x.score = int(input('重新输入分数'))
                        if not (0 <= x.score <= 100):
                            print('分数超出范围(0~100), 请重新输入')
                            continue
                        break
                    except:
                        print('分数输入错误, 请重新输入')
                        continue
                return
            elif i == 2:    # 重名则跳到下一个
                continue
            else:
                print('命令输入错误')
                return
    else:
        print('未找到'+_name)

def score_h(l):    # 由高到低
    s = sorted(l,key=(lambda n:n.get_score),reverse=True)
    print_student(s)

def score_l(l):    # 由低到高
    s = sorted(l,key=(lambda n:n.get_score))
    print_student(s)

def age_h(l):    # 由高到低
    s = sorted(l,key=(lambda n:n.get_age),reverse=True)
    print_student(s)

def age_l(l):    # 由低到高
    s = sorted(l,key = (lambda n:n.get_age))
    print_student(s)

def read_from_file():
    L = []
    try:
        f = open('si.txt','r')
        for line in f:
            line = line.strip()
            items = line.split(',')
            n, a, s = items
            a = int(a)
            s = int(s)
            L.append(Student(n, a, s))
        f.close()
    except OSError:
        print('打开文件失败')
    return L
    

def save_to_file(l):
    try:
        f = open('si.txt','w')
        for d in l:
            d.write_to_file(f)
        f.close()
    except OSError:
        print('保存文件失败')