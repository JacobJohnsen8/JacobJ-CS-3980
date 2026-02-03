def echo(text: str, repetitions: int = 3) -> str:
    "immitate a real world echo."
    print(text[-(repetitions):])
    print(text[-(repetitions- 1):])
    print(text[-(repetitions- 2):])
    print(".")

if __name__ == "__main__":
    text = input("Yell something into the mountians!: ")
    print(echo(text))
