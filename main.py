# Задание 1

# lst_ta1 = input('введите значение через пробел:')
# lst_ta1 = lst_ta1.split()
# print(lst_ta1)
# i = len(lst_ta1) - 1
#
# while i >= 0:
#     if lst_ta1[i].isdigit():
#         lst_ta1[i] = int(lst_ta1[i])
#     print(type(lst_ta1[i]))
#     i = i-1

# задание 2

# lst_ta2 = input('введите значение через пробел:')
# lst_ta2 = lst_ta2.split()
# i=0
# while i < len(lst_ta2)-1:
#     lst_ta2[i],lst_ta2[i + 1] = lst_ta2[i + 1],lst_ta2[i]
#     i = i+2
# print(lst_ta2)

# задание 3

# mon_dict = {12: "зима", 1: "зима", 2: "зима", 3: "весна", 4: "весна", 5: "весна", 6: "лето", 7: "лето", 8: "лето",
#             9: "осень", 10: "осень", 11: "осень"}
# mon_list = ["winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer",
#             "autumn", "autumn", "autumn", "winter"]
# print("введите номер месяца (от 1 до 12): ""\n")
# mon = int(input())
# print(mon_dict.get(mon))
# if (mon <= 12) and (mon > 0):
#     print(mon_list[mon - 1])

# задание 4

# print('введите значение через пробел: \n')
# lst_ta3 = input()
# lst_ta3 = lst_ta3.split()
#
# i = len(lst_ta3)
#
# for stoka in lst_ta3:
#     print(stoka[:10])

# задание 4

# lst_ta4 = [9, 7, 6, 5, 1]
# print('введите новый номер рейтинга: \n')
# rang = int(input())
# if rang in lst_ta4:
#     lst_ta4.insert(lst_ta4.index(rang), rang)
# else:
#     i = 0
#     for ind in lst_ta4[0:]:
#         if rang > int(ind):
#             lst_ta4.insert(i,rang)
#             break
#         i = i+1
# print(lst_ta4)

# задание 5
merch_base = []
merch = {"наименование": "", "цена":"", "количество":"", "ед":""}
stat = {"наименование": [], "цена":[], "количество":[], "ед":[]}
while 1:
    print("добавить товар - д, выход - н, п - печать базы, с - статистика")
    chuse = input().lower()
    if chuse == "н":
        break
    elif chuse == "д":
        i = len(merch_base)
        for mr in merch.keys():
            print("введите {}: ".format(mr))
            merch[mr] = input()
        merch_base.append((i+1, merch.copy()))
        print(merch_base[i])
    elif chuse == "п":
        for elem in merch_base:
            print(elem)
    elif chuse == "с":
        for elem in merch_base:
            for keys in stat:
                stat[keys].append(elem[1][keys])
        for keys in stat:
            print(keys)
            print(stat[keys])
        for keys in stat:
            stat[keys].clear()

    else:
        print("введите Д,Н,С или П")
