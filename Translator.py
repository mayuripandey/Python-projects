def translate(phrase):
    translation = ""
    for letters in phrase:
        if letters in "AEIOUaeiou":
            translation = translation+"m"
        else:
            translation = translation + letters
    return (translation)

print(translate(input("enter your phrase: ")))