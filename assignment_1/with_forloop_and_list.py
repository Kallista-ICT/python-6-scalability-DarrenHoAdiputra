# Step 1: Function to create one monster
def create_monster():
    # Asking for the monster's name
    name = input("What is the monster's name?")
    # Asking for the monster's HP
    hp = int(input("What is the monster's HP?"))
    # Asking for the monster's attack
    attack = int(input("What is the monster's attack power?"))
    # To return the monster as a dictionary
    return {"name": name, "hp": hp, "attack": attack}

# Step 2: Asking howmany monsters to create
num_monsters = int(input("How many monsters do you want to create?"))

# Step 3: Empty list to hold all monsters
monster_list = []

# Step 4: Use a "for" loop (w/ range) to create each monster
for i in range(num_monsters):
    print(f"\nCreating monster {i + 1}:")
    # Call the create_monster() function
    monster = create_monster()
    # Add the returned monster to the list
    monster_list.append(monster)

# Step 5: After the loop, print a summary of all monsters
print("\nSummary of created monsters:")
for i in range(num_monsters):
    monster = monster_list[i]
    print(f"{i + 1}. {monster['name']}, HP: {monster['hp']}, Attack: {monster['attack']}")
