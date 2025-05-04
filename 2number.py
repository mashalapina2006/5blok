def countLines(file_obj):  
    lines = file_obj.readlines()
    return len(lines)

def countChars(file_obj):  
    text = file_obj.read()
    return len(text)

def test(module_obj):
    """Вызывает функции подсчета и выводит результаты."""
    try:
        file_name = module_obj.__file__  
        with open(file_name, 'r', encoding='utf-8') as file:
            num_lines = countLines(file) 
            file.seek(0) 
            num_chars = countChars(file) 

        if num_lines is not None and num_chars is not None:
            print(f"Файл: {file_name}")
            print(f"Количество строк: {num_lines}")
            print(f"Количество символов: {num_chars}")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
    except Exception as e:
        print(f"Общая ошибка: {e}")

if __name__ == '__main__':
    test(mymod) 
