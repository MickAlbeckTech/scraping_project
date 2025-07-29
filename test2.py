list_of_lists = []
with open("micky.txt", "r") as file:
    for line in file:
        list_of_lists.append(line.strip().split("*"))

print(list_of_lists)


# TODO spend more time on understanding how this works
