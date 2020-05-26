with open("./user_file.txt", "r", encoding='utf-8')as file:
    s = [x.strip() for x in file.readlines()]
    # print(s)
    data = [i.split(",") for i in s]
    # print(data)
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(data[i][j])
            if "leiyh0804" in data[i][j] and "123456" in data[i][j]:
                print("登录成功")




# for i in range(len(data)):
    #     # for j in range(len(data[i])):
    #     #     # print(data[i][j])
    #     #     # print(data[i][0])
    #     #     # print(data[i][1])
    #     if "leiyh081104" in data[i][0] and "12345116" in data[i][1]:
    #         print("登录成功")
    #         break
    #     else:
    #         print("登录失败")
    #         continue











