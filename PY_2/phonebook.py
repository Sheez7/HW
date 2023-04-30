import re
import csv
from pprint import pprint
from collections import defaultdict

# Читаем адресную книгу в формате CSV в список contacts_list:
with open("Data.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

    # Привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999.
    phone_pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
                    r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
                    r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    phone_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\20'

    contacts_list_new = []
    for page in contacts_list:
        page_string = ','.join(page)
        format_page = re.sub(phone_pattern, phone_pattern_new, page_string)
        page_list = format_page.split(',')
        contacts_list_new.append(page_list)

    # Поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О.
    name_pattern = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                   r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
    name_pattern_new = r'\1\3\10\4\6\9\7\8'

    contacts_list = []
    for page in contacts_list_new:
        page_string = ','.join(page)
        format_page = re.sub(name_pattern, name_pattern_new, page_string)
        page_list = format_page.split(',')
        if page_list not in contacts_list:
            contacts_list.append(page_list)


# Объединить все дублирующиеся записи о человеке в одну.
new_list = defaultdict(list)
for info in contacts_list:
    key = tuple(info[:2])
    for item in info:
        if item not in new_list[key]:
            new_list[key].append(item)

result_list = list(new_list.values())

# Записать занные в новую адресную книгу
with open("phones.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(result_list)
    print('Done!')

# with open('phonebook.csv', unicode='utf=8') as f:
#     print(f.read())