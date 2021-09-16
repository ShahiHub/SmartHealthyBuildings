###Hello World!
###The file prints hello world! statement

import random

def print_bye(text):
    ###The function prints hello world
    ###input: string
    ###output: Boolean

    n = random.randint(1,25)
    for i in range(n):
        print(text)
    return True

def main():
    text = "Good Bye Cruel World!!!"
    print_bye(text)

if __name__=="__main__":
    main()
