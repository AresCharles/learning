import random
import re

#生成电话号码表
# str1 = "0123456789-()"
# with open('file.txt', 'w+') as a:
#     for i in range(1000000):
#         m = ''
#         num = random.randint(10, 13)
#         for i in range(num):
#             m += random.choice(list(str1))
#         a.write(m + "\n")

with open("file.txt", 'r') as a:
    while True:
        txt = a.readline()
        if not txt:
            break
        else:
            result = re.findall(r"\(\d{3}\)\d{3}-\d{4}|\d{3}\-\d{3}-\d{4}", txt)
            if result:
                print(result)                

