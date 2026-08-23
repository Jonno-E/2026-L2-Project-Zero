import math


# Functions go here
# C_01_Make_Statement_v3.py
def make_statement(statement, decoration, lines=1):
    """Creates headings (3 lines), subheadings (2 lines) and
    emphasised text / mini-headings (1 line). Only use emoji for
    single line statements"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


# Big instructions here
def instructions():
    print("Instructions:\n\nChoose a valid shape from the list presented\nInput the sizes asked for between 0.1 "
          "and 100,\nChoose to continue or exit.\nAll answers can be the first letters of words e.g: square (s)\n")


# C_05_integer_checker_between_v2.py
def int_check(question, low, high):
    """Check that users enter the integer value within a specified boundary."""

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


# C_04_string_checker_v2.py
def string_checker(question, valid_ans_list):
    """Checks that user enters the full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower().strip()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[0]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


# Lists
yes_no = ['yes', 'no']
shape_list = ['square', 'rectangle', 'circle', 'triangle', 'parallelogram']
exit_code = ["continue", "exit"]
history = []

# Main Routine starts here
print()
make_statement("Area | Perimeter Calculator", "-", 3)
print()

# Ask user if they want instructions
want_instructions = string_checker("Do you want to read the instructions? ", yes_no)

if want_instructions == "yes":
    instructions()
else:
    print(f"You chose no\n")


# Loop
while True:

    shape = string_checker("What shape would you like to calculate? "
                           "(square (s), rectangle (r), circle (c), triangle (t), parallelogram (p))", shape_list)

    print(f"you chose \n{shape}\n")
    # Square
    if shape == shape_list[0]:
        height = int_check("Enter the height of your shape:", 0.1, 100)
        area = height * height
        perimeter = height * 4
        history.append([shape, area, perimeter])
        print(f"\nThe area of the square is {area:.2f}")
        print(f"The perimeter of the square is {perimeter:.2f}")

    # Rectangle
    elif shape == shape_list[1]:
        height = int_check("Enter the height of your shape: ", 0.1, 100)
        length = int_check("Enter the length of your shape: ", 0.1, 100)
        area = height * length
        perimeter = 2 * height + 2 * length
        history.append([shape, area, perimeter])
        print(f"\nThe area of the rectangle is {area:.2f}")
        print(f"The perimeter of the rectangle is {perimeter:.2f}")

    # Circle
    elif shape == shape_list[2]:
        radius = int_check("Enter the radius of your shape: ", 0.1, 100)
        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius
        history.append([shape, area, circumference])
        print(f"\nThe area of the circle is {area:.2f}")
        print(f"The circumference of the circle is {circumference:.2f}")

    # Triangle
    elif shape == shape_list[3]:
        height = int_check("Enter the height of your shape: ", 0.1, 100)
        side_1 = int_check("Enter the side 1 / base of your shape: ", 0.1, 100)
        side_2 = int_check("Enter the side 2 of your shape: ", 0.1, 100)
        side_3 = int_check("Enter the side 3 of your shape: ", 0.1, 100)
        area = 0.5 * side_1 * height
        perimeter = side_1 + side_2 + side_3
        history.append([shape, area, perimeter])
        print(f"\nThe area of the triangle is {area:.2f}")
        print(f"The perimeter of the triangle is {perimeter:.2f}")

    # Parallelogram
    elif shape == shape_list[4]:
        base = int_check("Enter the base of your shape: ", 0.1, 100)
        side = int_check("Enter the side of your shape: ", 0.1, 100)
        height = int_check("Enter the height of your shape: ", 0.1, 100)
        area = base * height
        perimeter = 2 * (base + side)
        history.append([shape, area, perimeter])
        print(f"\nThe area of the parallelogram is {area:.2f}")
        print(f"The perimeter of the parallelogram is {perimeter:.2f}")

    # Ask user whether to continue or exit
    continue_or_exit = string_checker("\nWould you like to continue (c) or exit (e)? ", exit_code)

    if continue_or_exit == "exit":
        print("\nThanks for using Big calc\n\nSummary\n")

        # Give calculation history and exit
        for calculation in history:
            print(f"Shape: {calculation[0]}\nArea: {calculation[1]:.2f}\n"
                  f"Perimeter (circumference for circle): {calculation[2]:.2f}\n")
        break
