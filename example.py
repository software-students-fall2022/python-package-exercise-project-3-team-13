import team13hackertype.hackertype as hackertype
import team13hackertype.penetrate as penetrate


def main():
    loop_text = hackertype.looping_string('Hello, world!', 3)
    for i in range(10):
        print(next(loop_text))

    print("Here is part of a python snippet.")
    print(hackertype.get_code_snippet('python')[:30])

    hackertype.hackertype('python')
    print()

    penetrate.penetrate('python', text="WORDS!", loading_bar_speed=10)


if __name__ == '__main__':
    main()
