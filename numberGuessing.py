"""This file is a quiz testing math , english and science."""
import time
import sys
from colorama import Fore
from colorama import Back
import random

quizzing = 0
main_menu = 1
level_selection = 0
math_l1_turns = 0
math_l2_turns = 0
math_l3_turns = 0
frame_time = 0.2
first_time = 0
current_quiz_state = 0
math_max_turns = 10
reset = 0
loop_number = 1


def math_level_3():
    """Math level 3 question and answers."""
    num1 = random.randint(-150, 550)
    num2 = random.randint(-150, 550)
    op = random.choice(["+", "-", "*", "/"])

    x_answer = 0

    # Addition
    if op == '+':
        print(Fore.LIGHTBLUE_EX + Back.RESET)
        print(num1, "+", num2, "= x ")
        x_answer = str(num1 + num2)

    # Subtraction
    elif op == '-':
        print(Fore.LIGHTBLUE_EX + Back.RESET)
        print(num1, '-', num2, '= x')
        x_answer = str(num1 - num2)

    # Multiplication
    elif op == '*':
        print(Fore.LIGHTBLUE_EX + Back.RESET)
        print(num1, "*", num2, "= x")
        x_answer = str(num1 * num2)

    # Division
    elif op == "/":
        print(Fore.LIGHTBLUE_EX + Back.RESET)
        print(num1, "/", num2, "= x")
        x_answer = str(num1 / num2)

    else:
        print("Invalid Operator")

    x = input(Fore.BLACK + Back.WHITE + "What's x? ")

    if x_answer == x and x.isdigit:
        print(Fore.LIGHTGREEN_EX + Back.RESET+"Correct")
    else:
        print(Fore.LIGHTRED_EX + Back.RESET+"Incorrect")
        print(Fore.LIGHTGREEN_EX + Back.RESET+"Answer is", x_answer)

# Math level 2 question and answers


def math_level_2():
    """Math level 2 question and answers."""
    num1 = random.randint(40, 50)
    num2 = random.randint(10, 20)
    op = random.choice(["+", "-", "*", ])

    x_answer = 0
    # Addition
    if op == '+':
        print(Fore.LIGHTBLUE_EX + Back.RESET)
        print(num1, "+", num2, "= x ")
        x_answer = str(num1 + num2)

    # Subtraction
    elif op == '-':
        print(Fore.LIGHTBLUE_EX + Back.RESET)
        print(num1, '-', num2, '= x')
        x_answer = str(num1 - num2)

    # Multiplication
    elif op == '*':
        print(Fore.LIGHTBLUE_EX + Back.RESET)
        print(num1, "*", num2, "= x")
        x_answer = str(num1 * num2)

    else:
        print("Invalid Operator")

    x = input(Fore.BLACK + Back.WHITE + "What's x? ")

    if x == x_answer and x.isdigit:
        print(Fore.LIGHTGREEN_EX + Back.RESET+"Correct")
    else:
        print(Fore.LIGHTRED_EX + Back.RESET+"Incorrect")
        print(Fore.LIGHTGREEN_EX + Back.RESET+"Answer is", x_answer)


# Math level 1 question and answers
def math_level_1():
    """Math level 1 question and answers."""
    num1 = random.randint(10, 15)
    num2 = random.randint(0, 5)
    op = random.choice(["+", "-", "*", ])

    x_answer = 0

    # Addition
    if op == '+':
        print(Fore.LIGHTBLUE_EX + Back.RESET)
        print(num1, "+", num2, "= x ")
        x_answer = str(num1 + num2)

    # Subtraction
    elif op == '-':
        print(Fore.LIGHTBLUE_EX + Back.RESET)
        print(num1, '-', num2, '= x')
        x_answer = str(num1 - num2)

    # Multiplication
    elif op == '*':
        print(Fore.LIGHTBLUE_EX + Back.RESET)
        print(num1, "*", num2, "= x")
        x_answer = str(num1 * num2)

    # Level 1 and 2 do not have division

    else:
        print("Invalid Operator")

    x = input(Fore.BLACK + Back.WHITE + "What's x? ")

    if x == x_answer and x.isdigit:

        print(Fore.LIGHTGREEN_EX + Back.RESET+"Correct")
    else:
        print(Fore.LIGHTRED_EX + Back.RESET+"Incorrect")
        print(Fore.LIGHTGREEN_EX + Back.RESET+"Answer is", x_answer)


# Science level 1 question and answers
def science_l1():
    """Science level 2 question and answers."""
    class Question:
        def __init__(self, prompt, response):
            self.prompt = prompt
            self.response = response

    question_prompts = [
        "What is the chemical symbol of iron \n(a) 'Ir'\n(b)'Fi'\n(c) "
        "'Fe'\n", '\n'
        "How many electrons does hydrogen have?\n(a) 1\n(b) 6 \n(c) 2\n", '\n'
        "What is a neutral pH? \n(a) 10 \n(b) 7 \n(c) "
        "4\n", '\n'
        "What is the boiling point of water ? \n(a) 100°F  "
        "\n(b) 110°C \n(c) 100°C\n", '\n'
    ]
    questions = [
        Question(question_prompts[0], "c"),
        Question(question_prompts[1], "a"),
        Question(question_prompts[2], "b"),
        Question(question_prompts[3], "c"),
    ]
    for question in questions:
        print(Fore.RESET + Back.RESET)
        answer = input(question.prompt)
        if answer == question.response:
            print(Fore.LIGHTGREEN_EX + Back.RESET + "Correct!")
            print(Fore.RESET + Back.RESET)
        else:
            print(Fore.LIGHTRED_EX + Back.RESET + "Incorrect!")
            print(Fore.LIGHTGREEN_EX + Back.RESET +
                  "Answer is", question.response)
            print(Fore.RESET + Back.RESET)


# Science level 2 question and answers
def science_l2():
    """Science level 2 question and answers."""
    class Question:
        def __init__(self, prompt, response):
            self.prompt = prompt
            self.response = response

    question_prompts = [
        "What is the chemical formula of methane? "
        "\n(a) CH3 \n(b) CO2 \n(c) CH4 \n", '\n'
        "Which element has the atomic number 20? "
        "\n(a) Oxygen \n(b) Calcium \n(c) Iron\n", '\n'
        "What is the SI unit of force? \n(a) Newton"
        " \n(b) Joule \n(c) Watt\n", '\n'
        "What is the speed of light in a vacuum?"
        " \n(a) 300,000 km/s \n(b)"
        " 3,000 km/s \n(c) 30,000 km/s\n", '\n'
        "What is the chemical symbol for gold?"
        " \n(a) Go \n(b) Au \n(c) Ag\n", '\n'
    ]

    questions = [
        Question(question_prompts[0], "c"),
        Question(question_prompts[1], "b"),
        Question(question_prompts[2], "a"),
        Question(question_prompts[3], "a"),
        Question(question_prompts[4], "b"),
    ]
    for question in questions:
        print(Fore.RESET + Back.RESET)
        answer = input(question.prompt)
        if answer == question.response:
            print(Fore.LIGHTGREEN_EX + Back.RESET + "Correct!")
            print(Fore.RESET + Back.RESET)
        else:
            print(Fore.LIGHTRED_EX + Back.RESET + "Incorrect!")
            print(Fore.LIGHTGREEN_EX + Back.RESET +
                  "Answer is", question.response)
            print(Fore.RESET + Back.RESET)


# Science level 3 question and answers
def science_l3():
    """Science level 3 question and answers."""
    class Question:
        def __init__(self, prompt, response):
            self.prompt = prompt
            self.response = response

    question_prompts = [
        "What is the molecular formula of adrenaline? \n(a) C6H12O6"
        " \n(b) C9H13NO3 \n(c) CH4 \n", '\n'
        "Which of the following is a halogen element? \n(a) Sodium"
        " \n(b) Fluorine \n(c) Iron \n", '\n'
        "What is Planck's constant? \n(a) 6.626 × 10^-34 m^2 kg"
        " / s \n(b) 9.81 m/s^2 \n(c) 3 × 10^8 m/s \n", '\n'
        "Who discovered penicillin? \n(a) Alexander Fleming"
        " \n(b) Marie Curie \n(c) Albert Einstein \n", '\n'
        "What is the chemical formula of sulfuric acid?"
        " \n(a) HCl \n(b) H2SO4 \n(c) NaOH\n", '\n'
        "What is the charge of an electron? \n(a) +1"
        " \n(b) 0 \n(c) -1 \n", '\n'
        "What is the second law of thermodynamics? \n(a)"
        " Energy cannot be created or destroyed \n(b)"
        " Entropy tends to increase over time \n(c) Every "
        "action has an equal and opposite reaction\n",
        '\n'
        "What is the largest organ in the human body? "
        "\n(a) Liver \n(b) Skin \n(c) Heart\n", '\n'
        "Who proposed the theory of relativity? "
        "\n(a) Isaac Newton \n(b) Albert Einstein \n(c)"
        " Stephen Hawking \n", '\n'
        "What is the formula for calculating kinetic energy? "
        "\n(a) KE = mv \n(b) KE = 1/2 mv^2 \n(c) KE = Fd \n", '\n'
        "What is the main component of natural gas? \n(a)"
        " Methane \n(b) Ethane \n(c) Propane\n", '\n'
        "Which subatomic particle is responsible for chemical bonding?"
        " \n(a) Electron \n(b) Proton \n(c) Neutron \n",
        '\n'
        "What is the process by which plants make their own food? "
        "\n(a) Respiration \n(b) Photosynthesis \n(c) Fermentation\n",
        '\n'
        "What is the smallest unit of matter? \n(a) Atom "
        "\n(b) Molecule \n(c) Cell \n", '\n'
        "What causes tides in Earth's oceans? \n(a) "
        "Gravitational pull of the Moon \n(b) "
        "Gravitational pull of the Sun \n(c) Earth's rotation \n",
        '\n'
    ]
    questions = [
        Question(question_prompts[0], "b"),
        Question(question_prompts[1], "b"),
        Question(question_prompts[2], "a"),
        Question(question_prompts[3], "a"),
        Question(question_prompts[4], "b"),
        Question(question_prompts[5], "c"),
        Question(question_prompts[6], "b"),
        Question(question_prompts[7], "b"),
        Question(question_prompts[8], "b"),
        Question(question_prompts[9], "b"),
        Question(question_prompts[10], "a"),
        Question(question_prompts[11], "a"),
        Question(question_prompts[12], "b"),
        Question(question_prompts[13], "a"),
        Question(question_prompts[14], "a"),
    ]

    for question in questions:
        print(Fore.RESET + Back.RESET)
        answer = input(question.prompt)
        if answer == question.response:
            print(Fore.LIGHTGREEN_EX + Back.RESET + "Correct!")
            print(Fore.RESET + Back.RESET)
        else:
            print(Fore.LIGHTRED_EX + Back.RESET + "Incorrect!")
            print(Fore.LIGHTGREEN_EX + Back.RESET +
                  "Answer is", question.response)
            print(Fore.RESET + Back.RESET)

# English level 1 question and answers


def english_l1():
    """English level 1 question and answers."""
    class Question:
        def __init__(self, prompt, response):
            self.prompt = prompt
            self.response = response

    question_prompts = [
        "I spoke to ___  \n(a) 'she'\n(b)'there'\n(c) 'them'  \n", '\n'
        "Easter is ___ March this year.\n(a) on\n(b) in \n(c) at '\n' ", '\n'
        "I went ____ with my sister. \n(a) their \n(b) there \n"
        " they're\n", '\n'
        "The crime ___ is described as... \n(a) seen  \n(b)"
        " scene \n(c) sin\n", '\n'
    ]
    questions = [
        Question(question_prompts[0], "c"),
        Question(question_prompts[1], "a"),
        Question(question_prompts[2], "b"),
        Question(question_prompts[3], "c"),
    ]
    for question in questions:
        print(Fore.RESET + Back.RESET)
        answer = input(question.prompt)
        if answer == question.response:
            print(Fore.LIGHTGREEN_EX + Back.RESET + "Correct!")
            print(Fore.RESET + Back.RESET)
        else:
            print(Fore.LIGHTRED_EX + Back.RESET + "Incorrect!")
            print(Fore.LIGHTGREEN_EX + Back.RESET +
                  "Answer is", question.response)
            print(Fore.RESET + Back.RESET)


# English level 2 question and answers
def english_l2():
    """English level 2 question and answers."""
    class Question:
        def __init__(self, prompt, response):
            self.prompt = prompt
            self.response = response

    question_prompts = [
        "Which sentence is correct? \n(a) She goed to the"
        " store yesterday. \n"
        "(b) She goed to the store tomorrow. \n(c) "
        "She went to the store yesterday. \n"
        '\n',
        "What is the plural form of 'mouse'? \n(a) "
        "mouses \n(b) mouse \n(c) mice \n" '\n',
        "He ___ a good book last night. \n(a)"
        " readed \n(b) reads \n(c) read \n"
        '\n',
        "Which word is a preposition? \n(a) "
        "Quickly \n(b) Above \n(c) Dance \n" '\n',
        "What is the past tense of 'eat'? \n(a) "
        "eated \n(b) ate \n(c) eat \n" '\n',
        " They ___ to the beach every summer. "
        "\n(a) goes \n(b) go \n(c) at \n"
        '\n',
        "Which of the following sentences is"
        " an example of a compound sentence? \n"
        "(a) The dog barks loudly. \n(b) I "
        "like pizza, but my brother prefers pasta."
        " \n(c) She danced gracefully. \n"
        '\n',
        "What is the term for a word that "
        "replaces a noun? \n(a) Adjective \n(b) Verb \n(c) Pronoun \n" '\n',
        " Sarah ___ her homework every day. "
        "\n(a) do \n(b) does \n(c) did \n" '\n',
        "Which of the following sentences "
        "is an example of a complex sentence? \n"
        "(a) The sun shines brightly. "
        "\n(b) The cat slept on the mat. \n"
        "(c) After the rain stopped, "
        "we went outside to play. \n"
        '\n'
    ]

    questions = [
        Question(question_prompts[0], "c"),
        Question(question_prompts[1], "c"),
        Question(question_prompts[2], "c"),
        Question(question_prompts[3], "b"),
        Question(question_prompts[4], "b"),
        Question(question_prompts[5], "b"),
        Question(question_prompts[6], "b"),
        Question(question_prompts[7], "c"),
        Question(question_prompts[8], "b"),
        Question(question_prompts[9], "c")
    ]

    for question in questions:
        print(Fore.RESET + Back.RESET)
        answer = input(question.prompt)
        if answer == question.response:
            print(Fore.LIGHTGREEN_EX + Back.RESET + "Correct!")
            print(Fore.RESET + Back.RESET)
        else:
            print(Fore.LIGHTRED_EX + Back.RESET + "Incorrect!")
            print(Fore.LIGHTGREEN_EX + Back.RESET +
                  "Answer is", question.response)
            print(Fore.RESET + Back.RESET)


def loading():
    """This is the loading animation."""
    print(Fore.GREEN + Back.RESET+"Loading:")

    # Animation frames
    loading_animation = ["[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%",
                         "[■■■□□□□□□□] 30%",
                         "[■■■■□□□□□□] 40%",
                         "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%",
                         "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%",
                         "[■■■■■■■■■□] 90%",
                         '[■■■■■■■■■■] 100%']

    # Frame player
    for i in range(len(loading_animation)):
        time.sleep(frame_time)
        sys.stdout.write("\r" + loading_animation[i % len(loading_animation)])
        sys.stdout.flush()

    print("\n")


def english():
    """English text art."""
    print(Fore.MAGENTA + Back.RESET + """
        ╔═══╗─────╔╗────╔╗
        ║╔══╝─────║║────║║
        ║╚══╦═╗╔══╣║╔╦══╣╚═╗
        ║╔══╣╔╗╣╔╗║║╠╣══╣╔╗║
        ║╚══╣║║║╚╝║╚╣╠══║║║║
        ╚═══╩╝╚╩═╗╠═╩╩══╩╝╚╝
        ───────╔═╝║
        ───────╚══╝
        """)
    time.sleep(frame_time)

# Science text art


def science():
    """Science text art."""
    print(Fore.MAGENTA + Back.RESET + """
        ███████████████████████████████████████████
        █─▄▄▄▄█─▄▄▄─█▄─▄█▄─▄▄─█▄─▀█▄─▄█─▄▄▄─█▄─▄▄─█
        █▄▄▄▄─█─███▀██─███─▄█▀██─█▄▀─██─███▀██─▄█▀█
        ▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
        """)
    time.sleep(frame_time)


# Math text art
def math():
    """Math text art."""
    print(Fore.YELLOW + Back.RESET + """
        ███╗░░░███╗░█████╗░████████╗██╗░░██╗
        ████╗░████║██╔══██╗╚══██╔══╝██║░░██║
        ██╔████╔██║███████║░░░██║░░░███████║
        ██║╚██╔╝██║██╔══██║░░░██║░░░██╔══██║
        ██║░╚═╝░██║██║░░██║░░░██║░░░██║░░██║
        ╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝
        """)
    time.sleep(frame_time)


def welcome():
    """Welcome text art."""
    print(Fore.LIGHTBLUE_EX + Back.RESET + """
    ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
    ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
    ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
    ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
    ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
    ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝
     """)
    # Time between the welcome and the options menu
    time.sleep(frame_time)


# ask for the users name
while first_time == 0:
    name = input(Fore.BLACK + Back.WHITE + "1. What is your name?: ")
    if not name.isalpha():
        print(Fore.RED + Back.RESET + "Only letters are allowed!")
        first_time += 0
    else:
        first_time += 1

# Execute the loading animation
loading()
welcome()


# main menu

print(Fore.RESET + Back.RESET + "Your quiz options are")

while quizzing <= loop_number:
    # Quiz options
    print(Fore.RESET + Back.RESET + "1)Math")
    print(Fore.RESET + Back.RESET + "2)Science")
    print(Fore.RESET + Back.RESET + "3)English")
    quiz_selection =\
        input(Fore.BLACK + Back.WHITE + "What will it be: ")

    # Quiz subject selection
    if quiz_selection == "1":
        print(Fore.LIGHTGREEN_EX + Back.RESET + "OK, You selected...")
        math()
        current_quiz_state = 1
    elif quiz_selection == "2":
        print(Fore.LIGHTGREEN_EX + Back.RESET + "OK, You selected... ")
        science()
        current_quiz_state = 2
    elif quiz_selection == "3":
        print(Fore.LIGHTGREEN_EX + Back.RESET + "OK, You selected... ")
        english()
        current_quiz_state = 3
    else:
        print(Fore.RED + Back.RESET + "Invalid option")


# Check which math level the user wants
    if current_quiz_state == 1:
        current_quiz_state = reset
        print(Fore.RESET + Back.RESET + "Level 1")
        print(Fore.RESET + Back.RESET + "level 2")
        print(Fore.RESET + Back.RESET + "level 3")
        math_level_selection \
            = input(Fore.BLACK + Back.WHITE + "What will it be: ")

    # Math level 1
        if math_level_selection == "1":
            print(Fore.LIGHTGREEN_EX +
                  Back.RESET + "OK, You've selected Math level 1 ")
            math_l1_turns = reset
            while math_l1_turns <= math_max_turns:
                math_level_1()
                math_l1_turns += loop_number

        # Math level 2
        elif math_level_selection == "2":
            print(Back.RESET)
            print(
                Fore.LIGHTGREEN_EX + "OK, You've selected Math level 2 ")
            math_l2_turns = reset
            while math_l2_turns <= math_max_turns:
                math_level_2()
                math_l2_turns += loop_number

        # Math level 3
        elif math_level_selection == "3":
            print(
                Fore.LIGHTGREEN_EX + "OK, You've selected Math level 3 ")
            math_l3_turns = reset
            while math_l3_turns <= math_max_turns:
                math_level_3()
                math_l3_turns += loop_number

        else:
            print(Fore.RED + Back.RESET + "Invalid option")

    # Science Level selection
    elif current_quiz_state == 2:
        current_quiz_state = 0
        print(Fore.RESET + Back.RESET + "Level 1")
        print(Fore.RESET + Back.RESET + "level 2")
        print(Fore.RESET + Back.RESET + "level 3")
        science_level_selection = (
            input(Fore.BLACK + Back.WHITE + "What will it be: "))

        # Science level 1
        if science_level_selection == "1":
            print(Fore.LIGHTGREEN_EX +
                  Back.RESET + "OK, You've selected Science level 1 ")
            science_l1()
        # Science level 2
        elif science_level_selection == "2":
            print(Back.RESET)
            print(Fore.LIGHTGREEN_EX +
                  Back.RESET + "OK, You've selected Science level 2 ")
            science_l2()
        # Science level 3
        elif science_level_selection == "3":
            print(Back.RESET)
            print(Fore.LIGHTGREEN_EX +
                  "OK, You've selected Science level 3 ")
            science_l3()
        else:
            print(Fore.RED + Back.RESET + "Invalid option")

    # English Level selection
    elif current_quiz_state == 3:
        current_quiz_state = reset
        print(Fore.RESET + Back.RESET + "Level 1")
        print(Fore.RESET + Back.RESET + "level 2")

        english_level_selection = (
            input(Fore.BLACK + Back.WHITE + "What will it be: "))

        # English level 1
        if english_level_selection == "1":
            print(Back.RESET)
            print(Fore.LIGHTGREEN_EX +
                  "OK, You've selected English level 1 ")
            english_l1()
        # English level 2
        elif english_level_selection == "2":
            print(Fore.LIGHTGREEN_EX +
                  Back.RESET + "OK, You've selected Science level 2 ")
            english_l2()
        else:
            print(Fore.RED + Back.RESET + "Invalid option")
    else:
        print(Fore.RED + Back.RESET)
