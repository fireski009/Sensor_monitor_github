import random


def get_user_input():
    sensor_type = input("Enter sensor type: ")

    num_readings = int(input("How many readings do you want? "))
    minimum = float(input("Enter minimum value: "))
    maximum = float(input("Enter maximum value: "))
    threshold = float(input("Enter alert threshold: "))

    return sensor_type, num_readings, minimum, maximum, threshold


def generate_readings(num_readings, minimum, maximum):
    readings = []

    for i in range(num_readings):
        value = random.uniform(minimum, maximum)
        readings.append(value)

    return readings


def main():
    print("=== Sensor Data Analysis Tool ===")

    sensor_type, num_readings, minimum, maximum, threshold = get_user_input()

    readings = generate_readings(num_readings, minimum, maximum)

    print("\nGenerated Sensor Readings:")
    print(readings)


if __name__ == "__main__":
    main()