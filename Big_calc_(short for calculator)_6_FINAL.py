"""Calculate the area and perimeter of a shape chosen by the user."""
import math


def make_statement(statement, decoration, lines=1):
    """Create a heading or emphasised text using a decoration character.

    Creates headings (3 lines) and emphasised text / mini-headings
    (1 line). Only use decorations for single line statements.
    """
    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


def instructions():
    """Print an easily executable set of instructions."""
    print("Instructions:\n\nChoose a valid shape from the list presented\n"
          "Input the sizes asked for between 0.1 and 100,\n"
          "Choose to continue or exit.\n"
          "All answers can be the first letters of words e.g: "
          "square (s)\n")


def int_check(question, low, high):
    """Check that the user enters a number within a specified boundary.

    Keeps prompting until a valid number between low and high
    (inclusive) is entered, then returns it as a float.
    """
    error = (f"Oops - please enter a number that is higher "
             f"or equal to {low} and lower or equal to {high}.")

    while True:
        try:
            response = float(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def string_checker(question, valid_ans_list):
    """Check that the user enters a valid word or its first letter.

    Accepts either the full word or the first letter of a word from
    the list of valid responses.
    """
    while True:
        response = input(question).lower().strip()

        for item in valid_ans_list:
            # check if the response is the entire word or first letter
            if response == item or response == item[0]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


def record_result(shape_name, area_name, measure, measure_label="perimeter"):
    """Save a calculation to history and print the results."""
    history.append([shape_name, area_name, measure])
    print(f"\nThe area of the {shape_name} is {area_name:.2f}")
    print(f"The {measure_label} of the {shape_name} is {measure:.2f}")


# Lists used for string checker and storing calculation history
yes_no = ['yes', 'no']
shape_list = ['square', 'rectangle', 'circle', 'triangle', 'parallelogram']
exit_code = ["continue", "exit"]
history = []

# Main Routine starts here
# Prints statement - title
print()
make_statement("Area | Perimeter Calculator", "-", 3)
print()

# Ask user if they want instructions using string checker
want_instructions = string_checker(
    "Do you want to read the instructions? ", yes_no)

if want_instructions == "yes":
    instructions()
else:
    print("You chose no\n")


# Main Calculation Loop starts here
while True:

    shape = string_checker(
        "What shape would you like to calculate? (square (s), "
        "rectangle (r), circle (c), triangle (t), "
        "parallelogram (p))", shape_list)

    print(f"you chose \n{shape}\n")

    # Initialise variables for the shape calculations
    measure_name = "perimeter"
    area = 0
    perimeter = 0

    # Square Calculation: integer checker and calculations
    if shape == shape_list[0]:
        height = int_check("Enter the height of your shape: ", 0.1, 100)
        area = height * height
        perimeter = height * 4

    # Rectangle Calculation: integer checkers and calculations
    elif shape == shape_list[1]:
        height = int_check("Enter the height of your shape: ", 0.1, 100)
        length = int_check("Enter the length of your shape: ", 0.1, 100)
        area = height * length
        perimeter = 2 * height + 2 * length

    # Circle Calculation: integer checker and calculations
    elif shape == shape_list[2]:
        radius = int_check("Enter the radius of your shape: ", 0.1, 100)
        area = math.pi * radius ** 2
        perimeter = 2 * math.pi * radius
        measure_name = "circumference"

    # Triangle Calculation: integer checkers and calculations
    elif shape == shape_list[3]:
        height = int_check("Enter the height of your shape: ", 0.1, 100)
        side_1 = int_check(
            "Enter the side 1 / base of your shape: ", 0.1, 100)
        side_2 = int_check("Enter the side 2 of your shape: ", 0.1, 100)
        side_3 = int_check("Enter the side 3 of your shape: ", 0.1, 100)
        area = 0.5 * side_1 * height
        perimeter = side_1 + side_2 + side_3

    # Parallelogram Calculation: integer checkers and calculations
    elif shape == shape_list[4]:
        base = int_check("Enter the base of your shape: ", 0.1, 100)
        side = int_check("Enter the side of your shape: ", 0.1, 100)
        height = int_check("Enter the height of your shape: ", 0.1, 100)
        area = base * height
        perimeter = 2 * (base + side)

    # Save and display the result - handles every shape
    record_result(shape, area, perimeter, measure_name)

    # Ask user whether to continue or exit with string checker
    continue_or_exit = string_checker(
        "\nWould you like to continue (c) or exit (e)? ", exit_code)
    # If user picks continue, loops automatically, if user picks exit,
    # give calculation history and break
    if continue_or_exit == "exit":
        print("\nThanks for using Big calc\n\nSummary\n")

        # Give calculation history and exit
        for calculation in history:
            print(f"Shape: {calculation[0]}\nArea: {calculation[1]:.2f}\n"
                  f"Perimeter (circumference for circle): "
                  f"{calculation[2]:.2f}\n")
        break
