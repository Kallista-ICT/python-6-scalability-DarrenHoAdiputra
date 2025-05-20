# General greetings (hello)
def hello(name):
    return f"Hello, {name}!"

# Good morning greetings
def good_morning(name):
    return f"Good morning, {name}!"

# Good afternoon greetings
def good_afternoon(name):
    return f"Good afternoon, {name}!"

# Good evening greetings
def good_evening(name):
    return f"Good evening, {name}!"

# Seperate module
def main():
    print("This is the greeting module. Please run conversation.py.")

# The code below is for making sure that main() only runs when greeting.py is executed directly
if __name__ == "__main__":
    main()
