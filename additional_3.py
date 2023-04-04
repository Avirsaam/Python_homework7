# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

def index_of_second_ocurrence(input_list, lookup_string):
    if input_list.count(lookup_string) > 1:
        ocurrences = 0
        for i in range(len(input_list)):
            if lookup_string == input_list[i]:
                if ocurrences == 1:
                    return i
                else:
                    ocurrences += 1
    else:
        return -1


newlist = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
lookfor = "qwe"

print(index_of_second_ocurrence(newlist, lookfor))