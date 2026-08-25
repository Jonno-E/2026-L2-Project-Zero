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

# C03_yes_no_simple.py


def instructions():
    print("Instructions:")


def int_check(question, low, high):
    """Check that users enter the integer value within a specified boundary."""
    error = (f"Oops - please enter a number that is higher "
             f"or equal to {low} and lower or equal to {high} .")

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
    """Checks that user enter the full word
    or the 'n' letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[0]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


yes_no = ['yes', 'no']
shape_list = ['square', 'rectangle', 'circle', 'triangle', 'parallelogram']


# Main Routine starts here
print()
make_statement("Area | Perimeter Calculator", "-", 3)
print()

want_instructions = string_checker("Do you want to read the instructions? ", yes_no,)

if want_instructions == "yes":
    instructions()

elif want_instructions == "no":
    print(f"You chose {want_instructions}\n")

shape = string_checker("What shape would you like to calculate? ", shape_list,)

# Square
if shape == shape_list[0]:
    height = int_check("enter the height of your shape: ", 0.1, 100)
    shape = 'square'
    area = height * height
    perimeter = height * 4
    print(f'The area of the square is {area}')
    print(f'The perimeter of the square is {perimeter}')

# Rectangle
if shape == shape_list[1]:
    height = int_check("enter the height of your shape: ", 0.1, 100)
    length = int_check("enter the length of your shape: ", 0.1, 100)
    shape = 'rectangle'
    area = height * length
    perimeter = height * 2 + length * 2
    print(f'The area of the rectangle is {area}')
    print(f'The perimeter of the rectangle is {perimeter}')

# Circle
if shape == shape_list[2]:
    radius = int_check("enter the radius of your shape: ", 0.1, 100)
    shape = 'circle'
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    print(f'The area of the circle is {area}')
    print(f'The perimeter of the circle is {circumference}')

# Triangle
if shape == shape_list[3]:
    height = int_check("enter the height of your shape: ", 0.1, 100)
    side_1 = int_check("enter the side 1 / base of your shape: ", 0.1, 100)
    side_2 = int_check("enter the side 2 of your shape: ", 0.1, 100)
    side_3 = int_check("enter the side 3 of your shape: ", 0.1, 100)
    shape = 'triangle'
    area = 0.5 * side_1 * height
    perimeter = side_1 + side_2 + side_3
    print(f'The area of the triangle is {area}')
    print(f'The perimeter of the triangle is {perimeter}')

# Parallelogram
if shape == shape_list[4]:
    base = int_check("enter the base of your shape: ", 0.1, 100)
    side = int_check("enter the side of your shape: ", 0.1, 100)
    height = int_check("enter the height of your shape: ", 0.1, 100)
    shape = 'parallelogram'
    area = base * height
    perimeter = 2 * (base + side)
    print(f'The area of the parallelogram is {area}')
    print(f'The perimeter of the parallelogram is {perimeter}')

