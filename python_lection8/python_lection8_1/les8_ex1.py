import re
import os
import csv
from pathlib import Path


def get_data():
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта',
                  'Тип системы']]
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    from pathlib import Path
    directory = '..\python_lection8_1'
    pathlist = Path(directory).glob('*.txt')
    for path in pathlist:
        with open(path, 'r', encoding='utf-8') as file:
            data = file.read()
            file.close()
        print(path)

        os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
        os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])
        os_name_reg = re.compile(r'Название ОС:\s*\S*')
        os_name_list.append(os_name_reg.findall(data)[0].split()[2])
        os_code_reg = re.compile(r'Код продукта:\s*\S*')
        os_code_list.append(os_code_reg.findall(data)[0].split()[2])
        os_type_reg = re.compile(r'Тип системы:\s*\S*')
        os_type_list.append(os_type_reg.findall(data)[0].split()[2])

    for i in range(len(os_prod_list)):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i],os_type_list[i]])

    return main_data


def write_to_csv():
    data = get_data()

    my_f = open("data_report.csv", "w", encoding="utf-8")
    with my_f:
        writer = csv.writer(my_f)
        writer.writerows(data)

write_to_csv()
