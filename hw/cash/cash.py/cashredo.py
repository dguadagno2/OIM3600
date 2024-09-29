# Note: The chatGPT questions are recreated because when I first did the assignement I did not login and could not save the questions I asked so I attempted to recreate them
def get_cents() -> int:
    """
    Ask how many cents the customer is owed, and return the number
    """
    owed = input("How many cents is the customer owed >>")
    owed = int(owed)
    if owed > 0:
        print("The customer is owed", owed)
        return owed
    else:
        print("Please enter a positive value")
        return 0  # Asked ChatGPT why code was running incorrectly


def calculate_quarters(cents: int) -> int:
    """
    Calculate the number of quarters to give the customer
    """
    return (
        cents // 25
    )  # At first tried to run a loop that would subtract 25 each round and count the rounds, however I kept getting the error between nonetype and int and even tried to use chatGPT to debug but it did not help, I decided to rethink my approach I realized I could just divide, however I got stuck becuase it would not round to whole numbers so I asked chatpgt to make it round the numbers https://chatgpt.com/share/66f9abfe-2d80-8011-ab85-793b7988fee2


def calculate_dimes(cents: int) -> int:
    """
    Calculate the number of dimes to give the customer
    """
    return cents // 10


def calculate_nickels(cents: int) -> int:
    """
    Calculate the number of nickels to give the customer
    """
    return cents // 5


def calculate_pennies(cents: int) -> int:
    """
    Calculate the number of pennies to give the customer
    """
    return cents // 1


def main():
    """
    You don't need to change any code in this function
    """
    # Ask how many cents the customer is owed
    cents = get_cents()

    # Calculate the number of quarters to give the customer
    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25

    # Calculate the number of dimes to give the customer
    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    # Calculate the number of nickels to give the customer
    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    # Calculate the number of pennies to give the customer
    pennies = calculate_pennies(cents)
    cents = cents - pennies * 1

    # Sum coins
    coins = quarters + dimes + nickels + pennies

    # Print the total number of coins to give the customer
    print(f"The total number of coins is {coins}.")


if __name__ == "__main__":
    main()
