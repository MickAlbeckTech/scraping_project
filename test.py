data = [[1, 2, 3], ['a', 'b', 'c'], [True, False]]


with open("mick.txt", "w") as file:
    for sublist in data:
        new_sublist = []
        for item in sublist:
            new_sublist.append(str(item))
        new_sublist_str = "*".join(new_sublist) + "\n"
        file.write(new_sublist_str)


        # str_sublist = ",".join(str(item) for item in sublist) + "\n"

