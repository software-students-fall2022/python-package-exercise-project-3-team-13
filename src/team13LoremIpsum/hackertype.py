import keyboard


def looping_string(string: str, chunk_size: int):
    current_index = 0
    string_length = len(string)
    while True:
        chunk = ''
        for i in range(chunk_size):
            chunk += string[(current_index + i) % string_length]
        current_index = (current_index + chunk_size) % string_length
        yield chunk


def get_code_snippet(language: str) -> str:
    language_to_path = {
        'python': '../code_snippets/python.txt',
        'java': '../code_snippets/java.txt'
    }

    try:
        with open(language_to_path[language]) as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"No file for this language: {language}.")
    except IOError as ioe:
        raise IOError("Unexpected I/O error", ioe)
    except Exception as e:
        raise Exception("Unexpected exception", e)


def hackertype(language: str, speed: int = 5) -> None:
    '''
    Starts listening for keyboard presses. On key press,
    print out 'speed' amount of characters from a sample document
    written in the 'language' coding language.

    Parameters
    ----------
    language : str
        The coding language of the hacker type to be printed.
        Supported values include TODO: get supported languages
    speed : int, optional
        The number of characters to print out on a single key
        press. (Default is 5.)

    Returns
    -------
    None
    '''
    code_snippet = get_code_snippet(language)
    code_snippet_iter = looping_string(code_snippet, speed)
    keyboard.on_press(lambda e:
                      print(next(code_snippet_iter), end='', flush=True))
    keyboard.wait('esc')


if __name__ == '__main__':
    hackertype('python', speed=20)
