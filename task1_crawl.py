# coding=utf8

from pymongo import *

class DataManager(object):
    def __init__(self):
        conn = MongoClient()
        database = conn['people']
        self.col = database.workman
        self.method_dict = {1:self.findAll, 2:self.findOne, 3:self.add, 4:self.update, 5:self.delete, 6:self.exit}

        self.run()

    def run(self):
        while 1:
            self.show_menu()
            choice = self.getChoice()
            self.method_dict[choice]()

    def findOne(self):
        name = raw_input('请输入要查找的工人的姓名：')
        workman = self.col.find_one({'name': name})
        self.query_one(workman)

    def findAll(self):
        all = self.col.find({})
        for i, workman in enumerate(all):
            print '{0}: '.format(i+1),
            self.query_one(workman)

    def query_one(self, workman):
        for i in workman.keys():
            print '{0}-{1} '.format(i, workman[i]),
        print

    def add(self):
        print '----------------添加工人----------------'
        id = raw_input('请输入要添加的工人id：')
        name = raw_input('请输入要添加的工人姓名：')
        age = raw_input('请输入要添加的工人年龄：')
        sex = raw_input('请输入要添加的工人性别：')
        salary = raw_input('请输入要添加的工人工资：')
        self.col.insert({'id': id, 'name': name, 'age': age, 'sex': sex, 'salary': salary})

    def update(self):
        id = self.get_id()
        str = raw_input('请在【name, sex, age, salary】中选一个输入来指定要修改的信息：')
        while 1:
            if str == 'name':
                name = raw_input('请输入工人要修改名字为：')
                self.col.update_one({'id': id}, {'$set': {'name': name}})
                break
            elif str == 'sex':
                sex = raw_input('请输入工人要修改性别为：')
                self.col.update_one({'id': id}, {'$set': {'sex': sex}})
                break
            elif str == 'age':
                age = raw_input('请输入工人要修改年龄为：')
                self.col.update_one({'id': id}, {'$set': {'age': age}})
                break
            elif str == 'salary':
                salary = raw_input('请输入工人要修改工资为：')
                self.col.update_one({'id': id}, {'$set': {'salary': salary}})
                break
            else:
                str = raw_input('请在【name, sex, age, salary】中选一个输入来指定要修改的信息：')



    def get_id(self):
        while 1:
            str = raw_input('请输入要删除的工人的id（请输入数字）：')
            try:
                id = int(str)
                break
            except ValueError:
                print '输入的不是数字，不符合要求！'

        return str

    def delete(self):
        id = self.get_id()

        self.col.delete_one({'id': id})


    def exit(self):
        exit(1)

    def show_menu(self):
        print
        print
        print '***************************欢迎进入工人信息管理系统******************************'
        print '1.查询所有工人信息'
        print '2.查询特定工人信息'
        print '3.添加工人信息'
        print '4.修改工人信息'
        print '5.删除工人信息'
        print '6.退出'
        print '********************************************************************************'

    def getChoice(self):

        while 1:
            str = raw_input('请输入您的选择前面对应的序号（1-6）:')
            try:
                choice = int(str)
                if choice<1 or choice>6:
                    print '输入的数字不在要求的范围内！'
                else:
                    break
            except ValueError:
                print '输入的不是数字，不符合要求！'

        return choice



if __name__ == '__main__':
    DataManager()
