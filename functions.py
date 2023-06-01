def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{fio} | {phone}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    # print(data)
    data_to_find = input('Введите данные для поиска: ')
    print(search(data, data_to_find))


def search(book: str, info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    found_matches = []
    for contact in book:
        if info in contact:
            found_matches.append(contact)
    if len(found_matches) > 1:
        book = found_matches
        info = input('Введите больше символов: ')
        return search(book, info)
    if len(found_matches) == 1:
        return str(*found_matches)
    return 'Совпадений не найдено'   


def delete_info() -> None:
    """Находит в списке запись по определенному критерию поиска и удаляет ее"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    data_to_find = input('Введите данные для поиска записи, которую нужно удалить: ')
    for_delete = search(data, data_to_find)
    print(f'Запись {for_delete} будет удалена')
    data.remove(for_delete)
    data = '\n'.join(data)
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write(data)


def change_info() -> None:
    """Находит в списке запись по определенному критерию поиска 
       и заменяет найлденную запись на новую"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    data_to_find = input('Введите данные для поиска записи, которую нужно изменить: ')       
    for_change = search(data, data_to_find)
    print(f'Запись {for_change} будет изменена')
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    data[data.index(for_change)] = f'{fio} | {phone}'
    data = '\n'.join(data)
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write(data)