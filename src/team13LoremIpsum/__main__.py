import time
import src.team13LoremIpsum.hackertype as hackertype
import sys


def main(argv):
    # TODO: to add a new CL function, map the name of it
    #       to the function (from the appropriate module)
    functionMap = {
        "hackertype": hackertype.hackertype
    }
    command = argv[0]
    if (command in functionMap.keys()):
        try:
            functionMap[command](*argv[1:])
            time.sleep(1)  # gives time for threads to resolve
        except Exception as e:
            print(f"Incorrect use of command: {command}")
            print(str(e))
            sys.exit(1)
    else:
        print("Command not found in package")
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv[1:])
