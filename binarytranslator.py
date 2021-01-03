def binary(number):
    translator = ""
    for digits in number:
        if digits in "01":
            translator = translator + "3"
        else:
            translator = translator + digits
    return (translator)

print (binary(input("Enter the number : ")))
