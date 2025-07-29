lists = [["“That's the problem with drinking, I thought, as I poured myself a drink. If something bad happens you drink in an attempt to forget; if something good happens you drink in order to celebrate; and if nothing happens you drink to make something happen.”", 'Charles Bukowski', '/author/Charles-Bukowski'], ['“The truth." Dumbledore sighed. "It is a beautiful and terrible thing, and should therefore be treated with great caution.”', 'J.K. Rowling', '/author/J-K-Rowling']
]

with open("new_txt.txt", "w", encoding="utf-8") as file:
    for sub_list in lists:
        file.writelines(sub_list)
        file.write("\n")
        # sub_list_string = ",".join(sub_list)
        # print(sub_list_string)
        # file.write(sub_list_string)



with open("new_txt.txt", "r", encoding="utf-8") as file:
    file_str = file.read()
    print(file_str)
    


