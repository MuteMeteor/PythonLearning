#1.定义一个有列表的名字
names = ['Anna','Benny','Cindy']

#2.获取一个要查找的名字
insertName = input("input your name:")

#3.输出查找结果
findFlag = 0;
for name in names:
    if name == insertName:
        findFlag = 1

if findFlag == 1:
    print('Find it!')
else:
    print('Cannot get it!')
