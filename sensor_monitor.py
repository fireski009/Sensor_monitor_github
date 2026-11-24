import random
import csv
import numpy as np
import matplotlib.pyplot as plt

def get_user_input():

    sensor_type = input("Enter sensor type (temperature/light/etc.): ").strip()

    if not sensor_type:
        sensor_type = "Sensor"

    while True:
        try:
            num_readings = int(input("How many readings should be generated? "))

            if num_readings <= 0:
                print("Error: Number of readings must be greater than zero.")
                continue

            break

        except ValueError:
            print("Error: Please enter a whole number.")

    while True:
        try:
            minimum = float(input("Enter minimum sensor value: "))
            maximum = float(input("Enter maximum sensor value: "))

            if minimum >= maximum:
                print("Error: Minimum must be smaller than maximum.")
                continue

            break

        except ValueError:
            print("Error: Please enter numeric values.")

    while True:
        try:
            threshold = float(input("Enter alert threshold: "))
            break

        except ValueError:
            print("Error: Please enter a numeric threshold.")

    return sensor_type, num_readings, minimum, maximum, threshold


def generate_readings(num_readings, minimum, maximum):

    def generate_readings(num_readings, minimum, maximum):
    readings = []

    for i in range(num_readings):
        value = random.uniform(minimum, maximum)
        readings.append(value)

    return readings

    return readings

def calculate_statistics(readings, threshold):

    data = np.array(readings)

    above_threshold = data[data > threshold]

    print("\n--- Sensor Statistics ---")

    print(f"Number of readings: {len(data)}")
    print(f"Mean: {np.mean(data):.2f}")
    print(f"Minimum: {np.min(data):.2f}")
    print(f"Maximum: {np.max(data):.2f}")
    print(f"Standard deviation: {np.std(data):.2f}")

    print(
        f"Readings above threshold ({threshold}): "
        f"{len(above_threshold)}"
    )

    return above_threshold


def find_outliers(readings, threshold):

    outliers = [
        value for value in readings
        if value > threshold
    ]

    print("\nReadings exceeding the threshold:")

    if outliers:
        print([round(value, 2) for value in outliers])
    else:
        print("None")

    return outliers


def save_readings(readings, filename="sensor_readings.csv"):

    try:
        with open(filename, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(["Sample number", "Sensor reading"])

            for index, value in enumerate(readings, start=1):
                writer.writerow([index, value])

        print(f"Data saved to '{filename}'.")

    except OSError as error:
        print(f"Error saving CSV file: {error}")


def load_readings(filename):

    readings = []

    try:
        with open(filename, "r", newline="") as file:

            reader = csv.DictReader(file)

            if "Sensor reading" not in (reader.fieldnames or []):
                print("Error: CSV must contain a 'Sensor reading' column.")
                return None

            for row in reader:
                readings.append(float(row["Sensor reading"]))

        if not readings:
            print("Error: The CSV file contains no readings.")
            return None

        return readings

    except (OSError, ValueError, KeyError) as error:
        print(f"Error loading CSV file: {error}")
        return None


def plot_readings(readings, threshold, sensor_type):

    samples = range(1, len(readings) + 1)

    plt.figure()

    plt.plot(
        samples,
        readings,
        marker="o",
        label="Sensor readings"
    )

    plt.axhline(
        threshold,
        linestyle="--",
        label="Alert threshold"
    )

    plt.title(f"{sensor_type} Sensor Readings")
    plt.xlabel("Sample number")
    plt.ylabel("Sensor value")

    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()



def plot_histogram(readings, sensor_type):

    plt.figure()

    plt.hist(
        readings,
        bins=10,
        edgecolor="black"
    )

    plt.title(f"Distribution of {sensor_type} Readings")
    plt.xlabel("Sensor value")
    plt.ylabel("Frequency")

    plt.grid(True)

    plt.tight_layout()
    plt.show()


# 9. Main function
def main():

    print("=== Sensor Data Analysis Tool ===")

    print("1. Generate new sensor readings")
    print("2. Load readings from an existing CSV file")

    while True:

        choice = input("Choose 1 or 2: ").strip()

        if choice in ("1", "2"):
            break

        print("Invalid choice. Please enter 1 or 2.")

    # Option 1: Generate new readings
    if choice == "1":

        (
            sensor_type,
            num_readings,
            minimum,
            maximum,
            threshold
        ) = get_user_input()

        readings = generate_readings(
            num_readings,
            minimum,
            maximum
        )

        save_readings(readings)

    # Option 2: Load existing readings
    else:

        filename = input("Enter CSV filename to load: ").strip()

        readings = load_readings(filename)

        if readings is None:
            return

        sensor_type = (
            input("Enter sensor type for the plots: ").strip()
            or "Sensor"
        )

        while True:
            try:
                threshold = float(input("Enter alert threshold: "))
                break

            except ValueError:
                print("Error: Please enter a numeric threshold.")

    # Analyze and visualize the readings
    calculate_statistics(readings, threshold)

    find_outliers(readings, threshold)

    plot_readings(readings, threshold, sensor_type)

    plot_histogram(readings, sensor_type)


# 10. Program entry point
if __name__ == "__main__":
    main()
