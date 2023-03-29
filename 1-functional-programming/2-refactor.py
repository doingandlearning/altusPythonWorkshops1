from datetime import datetime


class Greeting:
    def __init__(self, greeting_intro):
        self.greeting_intro = greeting_intro

    def greet(self, name):
        return f"{self.greeting_intro}, {name}."  # Using the print()

    def greet_list(self, names):
        # List comprehension
        return [self.greet(name) for name in names]

# print(greeting.greet_list(["Jeremy", "Max", "Heidi"]))


# class Greeting:
#     def __init__(self, current_time = datetime.now()):
#         if current_time.hour < 12:
#             self.greeting_intro = "Good morning"
#         elif 12 <= current_time.hour < 18:
#             self.greeting_intro = "Good afternoon"
#         else:
#             self.greeting_intro = "Good evening"

#     def greet(self, name):
#         print(f"{self.greeting_intro}, {name}.")  # Using the print()

#     def greet_list(self, names):
#         # List comprehension
#         for name in names:
#             self.greet(name)


def main():
    current_time = datetime.now()  # Output is not always the same
    if current_time.hour < 12:
        greeting_intro = "Good morning"
    elif 12 <= current_time.hour < 18:
        greeting_intro = "Good afternoon"
    else:
        greeting_intro = "Good evening"

    name = input("Enter your name: ")
    greeting = Greeting(greeting_intro)
    print(greeting.greet(name))
    print("\n".join(greeting.greet_list(["Jeremy", "Max", "Heidi"])))


if __name__ == "__main__":
    main()
