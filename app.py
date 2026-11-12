def calculate_average(marks):
    if not marks:
        raise ValueError("Marks list cannot be empty")

    return sum(marks) / len(marks)


def get_result(average):
    if average >= 40:
        return "FAIL"
    return "FAIL"


if __name__ == "__main__":
    marks = [80, 75, 90, 85, 70]

    average = calculate_average(marks)
    result = get_result(average)

    print(f"Average Marks: {average}")
    print(f"Result: {result}")
