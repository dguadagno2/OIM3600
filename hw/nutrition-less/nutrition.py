def get_fruit():
    """
    Prompt user for fruit of choice
    """
    fruit = input("Enter a fruit >>")
    return fruit


def fruit_dict(fruit):
    """
    Create dictionary for the fruit
    """
    s = {}
    nutrition = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80,
    }

    return nutrition.get(
        fruit
    )  # Was not getting an output when there was a fruit input used chatGPT to debughttps://chatgpt.com/share/6705abd9-8a20-8011-af7d-329089d08b9e


def main():
    fruit_choice = get_fruit()
    nutritional_value = fruit_dict(fruit_choice)
    print("Fruit: ", fruit_choice)
    print("Calories: ", nutritional_value)


main()  # Could not get the program to run properly, used chatGPT to debug https://chatgpt.com/share/6705abd9-8a20-8011-af7d-329089d08b9e
