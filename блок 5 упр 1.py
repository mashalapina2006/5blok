def countLines(name):
    """Counts the number of lines in a file."""
    try:
        with open(name, 'r') as file:
            lines = file.readlines()
        return len(lines)
    except FileNotFoundError:
        return f"Error: File '{name}' not found."
    except Exception as e:
        return f"Error: An error occurred: {e}"

def countChars(name):
    """Counts the number of characters in a file."""
    try:
        with open(name, 'r') as file:
            data = file.read()
        return len(data)
    except FileNotFoundError:
        return f"Error: File '{name}' not found."
    except Exception as e:
        return f"Error: An error occurred: {e}"

def test(name):
    """Tests the countLines and countChars functions with the given file."""
    lines = countLines(name)
    chars = countChars(name)
    return (lines, chars)

if __name__ == '__main__':
    filename = "mymod.py"

    line_count = countLines(filename)
    char_count = countChars(filename)

    print(f"File: {filename}")
    print(f"Lines: {line_count}")
    print(f"Characters: {char_count}")
