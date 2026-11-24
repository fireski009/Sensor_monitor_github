import random
import numpy as np

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

def calculate_statistics(readings, threshold):
    data = np.array(readings)

    mean_value = np.mean(data)
    minimum = np.min(data)
    maximum = np.max(data)
    standard_deviation = np.std(data)

    above_threshold = data[data > threshold]

    print("\n--- Sensor Statistics ---")
    print("Number of readings:", len(data))
    print("Mean:", round(mean_value, 2))
    print("Minimum:", round(minimum, 2))
    print("Maximum:", round(maximum, 2))
    print("Standard deviation:", round(standard_deviation, 2))
    print("Readings above threshold:", len(above_threshold))

    return above_threshold

def find_outliers(readings, threshold):
    outliers = []

    for value in readings:
        if value > threshold:
            outliers.append(value)

    print("\nReadings above alert threshold:")

    if len(outliers) > 0:
        print(outliers)
    else:
        print("No alerts detected.")

    return outliers

def main():
    print("=== Sensor Data Analysis Tool ===")

    sensor_type, num_readings, minimum, maximum, threshold = get_user_input()

    readings = generate_readings(num_readings, minimum, maximum)

    print("\nGenerated Sensor Readings:")
    print([round(value, 2) for value in readings])

    calculate_statistics(readings, threshold)

    find_outliers(readings, threshold)


if __name__ == "__main__":
    main()