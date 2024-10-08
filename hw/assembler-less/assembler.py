def assembler(program):
    """
    Assemble and execute a simple program represented as a list of instructions.

    Parameters:
        program (list): A list of strings representing the program instructions.

    Returns:
        int: The final value of the register after executing all the instructions in the program.
    """
    register = 0
    for (
        instruction
    ) in (
        program
    ):  # could not get the program to run properly specifically ran into difficulty with iterating and splitting the variables in the string, used ChatGPT to debug https://chatgpt.com/share/6705a9c9-1ee4-8011-9fca-f5b2391b003e
        operator, value = instruction.split()
        value = int(value)
    if operator == "inc":
        register += value
    elif operator == "dec":
        register -= value
    return register


# DO NOT CHANGE CODE BELOW!!!
def main():
    """TESTING CODE"""
    program = ["dec 8", "inc 7", "inc 6", "dec 3", "inc 8", "dec 2"]
    result = assembler(program)
    print(result)  # 8


if __name__ == "__main__":
    main()
