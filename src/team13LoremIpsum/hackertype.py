import keyboard

# TODO: I don't think I need this class if I have the iterator function
#       Create tests for the function to see if it works


class LoopingString:
    '''
    A wrapper class for a string that allows users to access substrings
    of size 'chunk_size' forever.
    '''
    def __init__(self, string: str, chunk_size: int) -> None:
        '''
        Initializer for LoopingString.

        Parameters
        ----------
        string: str
            The string to loop through
        chunk_size: int
            The number of characters to return for each iteration

        Returns
        -------
        None
        '''
        self.string = string
        self.chunk_size = chunk_size

    def __iter__(self):
        self.string_length = len(self.string)
        self.current_index = 0
        return self

    def __next__(self) -> str:
        # circular array implementation
        chunk = ''
        for i in range(self.chunk_size):
            chunk += self.string[(self.current_index + i) % self.string_length]
        self.current_index = (self.current_index + self.chunk_size) \
            % self.string_length
        return chunk


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
