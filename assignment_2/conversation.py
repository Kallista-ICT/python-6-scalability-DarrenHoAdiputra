import greeting

# Main part of the code
def main():
    name = input("What's your name? ")
    time = int(input(f"{name}, what time is it now? My clock is not working. (format hh) "))

    if 5 <= time < 12:
        message = greeting.good_morning(name)
    elif 12 <= time < 17:
        message = greeting.good_afternoon(name)
    elif 17 <= time <= 23:
        message = greeting.good_evening(name)
    else:
        message = greeting.hello(name)

    print(f"{message} Thank you for your assistance. Appreciate it.")

if __name__ == "__main__":
    main()
