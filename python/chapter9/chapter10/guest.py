while True:
    name = input('输入你的名字,退出输入N')
    if name == 'N':
        break
    else:
        print("thank you "+name)
        filename = 'python/chapter9/chapter10/programming.txt'
        with open(filename, 'a') as name_store:
            name_store.write(name+"logined\n")
