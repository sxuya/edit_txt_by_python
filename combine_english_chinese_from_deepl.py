from time import strftime

time_string = strftime("%Y.%m.%d_%H.%M.%S")
en_ls = []
ch_ls = []
result_name = 'result_'+time_string+".txt"

with open(result_name, 'w', encoding='utf-8') as result:
    with open('english.txt', 'r', encoding='utf-8') as english:
        en_ls = english.readlines()
#         print(en_ls[0])
#         print(en_ls[1])
#         print(en_ls[2])
#         print(english.readlines())
#         print(english.readlines()[0])
#         print(english.readlines()[1])
#         print(english.readlines()[2])
#         print(len(english.readlines()))
        
        with open('chinese.txt', 'r', encoding='utf-8') as chinese:
            ch_ls = chinese.readlines()
            for i in range(0, len(en_ls), 1):
                if en_ls[i] != '\n':
                    result.write(en_ls[i])
                    result.write(ch_ls[i])
                    result.write('\n') # 成功！2021年12月01日 00:24:51
#             print(len(chinese.readlines()))
            
#             print(english.readlines()[22])
#             for i in range(len(english.readlines())):
#                 result.write(english.readlines()[i])
#                 result.write(chinese.readlines()[i])
