# Introductory Statistics Module
# This module provides short lessons with questions and explanations.
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def ask(question, correct_answer, explanation):
    """Ask the user a question and provide explanation."""
    user_answer = input(question + " ")
    try:
        if float(user_answer) == correct_answer:
            print("Correct!" )
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")
    except ValueError:
        print(f"Invalid input. The correct answer is {correct_answer}.")
    print(explanation)
    print()


def lesson_mean():
    print("Lesson: Mean")
    numbers = [2, 4, 6, 8, 10]
    mean_val = sum(numbers) / len(numbers)
    print(f"Example: numbers = {numbers}")
    print(f"Mean = {mean_val}")
    plt.bar(range(len(numbers)), numbers)
    plt.title("Numbers")
    plt.show()
    ask("What is the mean of [1, 3, 5, 7]?", 4, "Add the numbers and divide by the count: (1+3+5+7)/4 = 4")


def lesson_median():
    print("Lesson: Median")
    numbers = [1, 2, 5, 7, 8]
    print(f"Example: numbers = {numbers}")
    median_val = numbers[len(numbers) // 2]
    print(f"Median = {median_val}")
    plt.bar(range(len(numbers)), numbers)
    plt.title("Numbers")
    plt.show()
    ask("What is the median of [3, 1, 4]?", 3, "Sort the numbers [1,3,4] and choose the middle value: 3")


def lesson_variance():
    print("Lesson: Variance")
    data = [2, 4, 4, 4, 5, 5, 7, 9]
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    print(f"Example data: {data}")
    print(f"Variance = {variance}")
    plt.hist(data, bins=range(min(data), max(data)+1))
    plt.title("Data Distribution")
    plt.show()
    ask("What is the variance of [1, 1, 1, 1]?", 0, "All numbers are the same, so variance is 0")


def run_module():
    print("Welcome to Introductory Statistics!")
    lessons = [lesson_mean, lesson_median, lesson_variance]
    for lesson in lessons:
        lesson()
    print("End of module.")


if __name__ == "__main__":
    run_module()
