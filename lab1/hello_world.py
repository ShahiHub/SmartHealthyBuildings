###Hello World!
###The file prints hello world! statement


def print_hello(text):
    ###The function prints hello world
    ###input: string
    ###output: Boolean

    print(text)
    return True

def main():
    text = "Hello World!"
    print_hello(text)

if __name__=="__main__":
    main()
