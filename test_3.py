import random
import numpy as np 
import csv
import matplotlib.pyplot as plt

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

def calculate_statistics(readings, threshold): #this function calculates the mean, min, max, and standard deviation of the sensor readings using NumPy. 
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

def find_outliers(readings, threshold): #this function specifically looks for readings that exceed the alert threshold given by the user.
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

def save_readings(readings, filename): #this function saves the generated sensor readings to a CSV file, with each reading on a new line along with its corresponding sample number.
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file) #"writer" function is used to write data to a CSV file.

        writer.writerow(["Sample number", "Sensor reading"])

        for index, value in enumerate(readings, start=1):
            writer.writerow([index, value]) #"writerow" function writes a single row to the CSV file, with the sample number and sensor reading.

    print("Data saved successfully!")

def load_readings(filename):
    readings = []

    with open(filename, "r", newline="") as file: #'r' is read mode
        reader = csv.DictReader(file) #this reads the csv file from the start of each row, using a column header

        for row in reader:
            value = float(row["Sensor reading"])
            readings.append(value)

    print("Data loaded successfully!")

    return readings

def main():
    print("=== Sensor Data Analysis Tool ===")

    print("1. Generate new readings")
    print("2. Load readings from CSV")

    choice = input("Choose an option: ")

    if choice == "1":
        sensor_type, num_readings, minimum, maximum, threshold = get_user_input()

        readings = generate_readings(num_readings, minimum, maximum)

        print("\nGenerated Sensor Readings:")
        print([round(value, 2) for value in readings])

        filename = input("Enter filename to save: ")
        save_readings(readings, filename)

    elif choice == "2":
        filename = input("Enter CSV filename to load: ")

        try:
            readings = load_readings(filename)

            sensor_type = input("Enter sensor type: ")
            threshold = float(input("Enter alert threshold: "))

        except FileNotFoundError:
            print("Error: File not found.")
            return

        except (ValueError, KeyError):
            print("Error: Invalid CSV data.")
            return

    else:
        print("Invalid choice.")
        return

    calculate_statistics(readings, threshold)

    find_outliers(readings, threshold)


if __name__ == "__main__":
    main()