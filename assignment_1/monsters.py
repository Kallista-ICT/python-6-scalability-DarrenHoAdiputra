# Main coding
def create_monster(order):
    print(f"Let's create the {order} monster!")
    name = input("What's the monster's name? ")
    hp = input("What's the monster's HP? ")
    attack = input("What's the monster's attack power? ")
    print(f"Monster created: {name}, HP: {hp}, Attack: {attack}\n")

# Creating two monsters (first and second monster)
create_monster("first")
create_monster("second")