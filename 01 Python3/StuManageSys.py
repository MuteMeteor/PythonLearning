
stuInfos = []
while True:
	
        #1.打印功能提示
        print('='*30)
        print("      学生管理系统v1.0")
        print('1.添加学生信息')
        print('2.删除学生信息')
        print('3.修改学生信息')
        print('4.查询学生信息')
        print('5.显示所有学生信息')
        print('0.退出系统')
        print('='*30)

        #2.获取功能的选择
        key = input('请输入功能对应的数字：')

        #3.根据用户选择，进行相应操作
        if key == '1':
            #添加学生信息
            #1.1 提示并获取学生姓名
            newName = input('请输入新学生姓名：')
            
            #1.2 提示并获取学生性别
            newSex = input('请输入新学生性别：')
            
            #1.3 提示并获取学生手机号码
            newPhone = input('请输入新学生手机号码：')

            newInfo = {}
            newInfo['name'] = newName
            newInfo['sex'] = newSex
            newInfo['phone'] = newPhone
            
            stuInfos.append('newInfo')

        elif key == '3':
            #修改学生信息
            #3.1 提示并修改
            
        elif key == '5':
            print('='*30)
            print('学生信息如下：')
            print('='*30)
            print('序号     姓名      性别       手机号码')
            print tempInfo in stuInfo:
            print('%d        %s        %s          %s' %(i,tempInfo[0][name],tempInfo[0][sex],tempInfo[0][phone]))
    
