data = [[1, 2, 3], ['a', 'b', 'c'], [True, False]]


# with open("mick.txt", "w") as file:
#     for sublist in data:
#         new_sublist = []
#         for item in sublist:
#             new_sublist.append(str(item))
#         print(new_sublist)
#         new_sublist_str = "*".join(new_sublist) + "\n"
#         print(new_sublist_str)
#         file.write(new_sublist_str)
        
with open("micky.txt", "w") as file:
    for sub_list in data:
        str_sublist = ",".join(str(item) for item in sub_list) + "\n"
        file.write(str_sublist)




