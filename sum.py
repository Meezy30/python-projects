def countdown_and_sum():
    total_sum = 0
    print("Counting down from 5 to 1:")
    for number in range(5, 0, -1):
        print(number)
        total_sum += number
    print(f"The sum of the countdown is: {total_sum}")

if __name__ == "__main__":
    countdown_and_sum()