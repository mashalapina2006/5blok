def countLines(file):
    """Подсчитывает количество строк в открытом файле."""
    lines = file.readlines()
    return len(lines)

def countChars(file):
    """Подсчитывает количество символов в открытом файле."""
    text = file.read()
    return len(text)

def test(name):
    """Вызывает функции подсчета и выводит результаты."""
    try:
        with open(name, 'r', encoding='utf-8') as file:
            num_lines = countLines(file) 
            file.seek(0) 
            num_chars = countChars(file) 

        if num_lines is not None and num_chars is not None:
            print(f"Файл: {name}")
            print(f"Количество строк: {num_lines}")
            print(f"Количество символов: {num_chars}")
    except FileNotFoundError:
        print(f"Файл '{name}' не найден.")
    except Exception as e:
        print(f"Общая ошибка: {e}")


if __name__ == '__main__':
    test("mymod.py")
