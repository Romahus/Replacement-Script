import os

def find_file(file_name, search_path):
    for root, dirs, files in os.walk(search_path):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

def replace_quotes(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        
        replaced_content = content.replace('"', '-')
        
        with open(file_name, 'w') as file:
            file.write(replaced_content)
        
        print(f'Кавычки успешно заменены в файле {file_name}')
    except FileNotFoundError:
        print(f'Файл {file_name} не найден')

if __name__ == '__main__':
    file_name = input('Введите имя файла: ')
    found_file = find_file(file_name, '/')
    if found_file:
        replace_quotes(found_file)
    else:
        print(f'Файл {file_name} не найден')
