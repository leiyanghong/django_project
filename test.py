# with open("./user_file.txt", "r", encoding='utf-8')as file:
#     s = [x.strip() for x in file.readlines()]
#     # print(s)
#     data = [i.split(",") for i in s]
#     # print(data)
#     for i in range(len(data)):
#         for j in range(len(data[i])):
#             print(data[i][j])
#             if "leiyh0804" in data[i][j] and "123456" in data[i][j]:
#                 print("登录成功")




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



import re


def main():
    content = 'Hello, I am Jerry, from Chongqing, a montain city, nice to meet you……'
    regex = re.compile('\w*o\w*')
    y = regex.match(content)
    print(y)
    print(type(y))
    print(y.group())
    print(y.span())

def a():
    white_list = "v02/login/"
    request_url = "v02/login/"
    r = re.compile(white_list)
    print(r)
    if r.match(request_url):

        print(r.match(request_url))
        y = r.match(request_url)
        print(y.group())
        print(y.span())
    else:
        print("no")
if __name__ == '__main__':
    a()






