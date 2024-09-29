# Note: The chatGPT questions are recreated because when I first did the assignement I did not login and could not save the questions I asked so I attempted to recreate them
def get_height():
    """
    Get the height of pyramid
    """
    height = input("Input a number between 1 and 8 >>")
    height = int(height)
    return height


def create_pyramid(height):
    """
    Generate Pyramid based on input
    """
    print("Height:", height)
    if height in range(1, 9):
        for i in range(1, height + 1):
            for j in range(height - i):
                print(" ", end="")
            for n in range(
                i
            ):  # Asked ChatGPT to debug my code as I had difficulty getting my pyramid to shift to the other side https://chatgpt.com/share/66f9b0e7-8080-8011-9255-9f93c40e4460
                print("#", end="")
            print()
    else:
        print("Please enter a number between 1 and 8")


def main():  # Asked Chat GPT to debug my code when I added defmain https://chatgpt.com/share/66f9b0e7-8080-8011-9255-9f93c40e4460
    height = get_height()
    create_pyramid(height)


main()
