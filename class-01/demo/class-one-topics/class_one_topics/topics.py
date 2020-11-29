"""Things to cover...
* What is a module
* What is a script
* How to execute it from CLI
* print/input
* string concatenation
* formatted strings
* if __name__ == "__main__": snippet
"""


some_secret_num = 9

def input_output():
    print("no console.log for me!")

    print("that's the standard output")

    print("but what about input?")

    color = input("what's my favorite color?")

    color_response = "Your favorite color is " + color + ". Great choice!"

    print(color_response)


    age = input("What's your age? ")

    formatted_string = f"You're favorite color is {color} and you are {age} years old"

    print(formatted_string)


    faves_template = "Your two favorite colors are {} and you are {} years old"

    print(faves_template)

    print(faves_template.format(color, age))

    print("my fav color is %s and I'm %d years old" %(color, int(age)))


def string_methods():
    print("sometimes you have a string with whitespace around it that you want trimmed")

    print("Python has a lot of nice built in methods for stuff like that")

    string_with_white_space = "\n\tspam and eggs\n"

    print(string_with_white_space)

    print(string_with_white_space.strip())


if __name__ == "__main__": # Get excuted when run as a script
    print("I was executed directly as a 'script'")
    print("Try making an 'importer.py' script that imports from me and see what happens")
    print("When you're done here head over to next demo and we'll play a game")
