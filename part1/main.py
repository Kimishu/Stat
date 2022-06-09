import csv
import pandas as pd
import numpy as np
from stats import complex_explore
from splitters import split_to_intervals


def explore(csv_file: str) -> None:
    """Explore csv file. Process it statistics information."""

    data = []

    with open(csv_file, 'r') as file:

        reader = csv.reader(file)
        for row in reader:
            data = [float(i) for i in row]

    complex_explore(data)


def main():
    explore('set_1.csv')


if __name__ == '__main__':
    main()
