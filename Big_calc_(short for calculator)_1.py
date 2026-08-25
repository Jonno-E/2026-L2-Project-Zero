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


def string_checker(question, valid_ans_list, num_letters):
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
shape_list = ['rectangle', 'circle', 'triangle', 'parallelogram']

# Main Routine goes here
print()
make_statement("Area | Perimeter Calculator", "-", 3)
print()

want_instructions = string_checker("Do you want to read the instructions? ", yes_no, 1)

if want_instructions == "yes":
    instructions()

elif want_instructions == "no":
    print(f"You chose {want_instructions}\n")

shape = string_checker("What shape would you like to calculate? ", shape_list, 3)

