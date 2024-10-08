def is_valid(s):
    """
    Checks that vanity plate meets the eligibillity requirements
    """
    # String is between 2-6 characters
    if not (2 <= len(s) <= 6):
        return False  # At first I tried to utilize return true for all but it did not work so I debugged with chatGPT https://chatgpt.com/share/670541ca-a81c-8011-8f0e-fb682975198e
    # String starts with two letters
    if not s[:2].isalpha():
        return False
    # First Number is not zero
    for char in s:
        if char.isdigit():
            if char == "0":
                return False
            break
    # If numbers are present in code must be at end of string
    num = False  # When testing my code I could not get the code to return valid for instances with any numbers, as such I used chatGPT to debug https://chatgpt.com/share/670541ca-a81c-8011-8f0e-fb682975198e
    for i in range(len(s)):
        if s[i].isdigit():
            num = True
        elif num and s[i].isalpha():
            return False
    # No periods, spaces, or punctuation marks
    if not s.isalnum():
        return False
    return True


def main():
    """
    Asks for input and returns valid or invalid
    """
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
