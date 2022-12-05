
def say_hello_to_stranger(name):
    message = "Hello " + name
    return message

def say_hello_to_friend(name):
    message = "Hello my friend, " + name
    return message

def main():
    person = input("What is your name? ")
    names = "Batman", "Superman", "Wonder Woman", person
    for name in names:
        if name == "Vic":
            message = say_hello_to_friend(name)
            print(message)
        else:
            message = say_hello_to_stranger(name)
            print(message)

main()