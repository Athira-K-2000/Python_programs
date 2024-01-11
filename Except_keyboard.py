#write a python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input

def keyboard_interrupt():

    try:
        a = int(input("Enter the number :"))

    except KeyboardInterrupt:
        print("Keyboard interrupt exception ")

keyboard_interrupt()
