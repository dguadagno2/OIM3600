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
            for n in range(i):
                print("#", end="")

            print(
                " ", end=""
            )  # Used ChatGPT to review my code and explain why my code was printing on the line below and why there was no space https://chatgpt.com/share/66f9a812-6fc8-8011-b811-02e828c52c9d
            for n in range(i):
                print("#", end="")
            print()
    else:
        print("Please enter a number between 1 and 8")


def main():  # Asked Chat GPT to debug my code
    height = get_height()
    create_pyramid(height)


main()
