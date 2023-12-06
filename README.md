# Weather Man

Weather Man is a command-line application that generates various reports based on weather data files.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Highest/Lowest Temperature and Most Humid Day for a Given Year](#1-highestlowest-temperature-and-most-humid-day-for-a-given-year)
  - [Average Temperatures and Humidity for a Given Month](#2-average-temperatures-and-humidity-for-a-given-month)
  - [Horizontal Bar Charts for Highest and Lowest Temperatures by Day in a Month](#3-horizontal-bar-charts-for-highest-and-lowest-temperatures-by-day-in-a-month)
- [Contributing](#contributing)

## Installation

To run Weather Man, ensure you have Python installed on your system.

Clone the repository:

```bash
git clone https://github.com/AhsanNazeef/Weatherman-Python.git
cd Weatherman-Python
```

## Usage

Weather Man supports several commands and options to generate different reports:

### 1. Highest/Lowest Temperature and Most Humid Day for a Given Year

```bash
python3 index.py -e 2002 /path/to/filesFolder
```
<img width="506" alt="image" src="https://github.com/AhsanNazeef/Weatherman-Python/assets/51314116/906cb18a-30cb-441d-ab0c-9d3237642b45">

### 2. Average Temperatures and Humidity for a Given Month

```bash
python3 index.py -a 2005/6 /path/to/files
```
<img width="482" alt="image" src="https://github.com/AhsanNazeef/Weatherman-Python/assets/51314116/7e350b08-3fd7-4c44-873b-0267b7ec7b07">

### 3. Horizontal Bar Charts for Highest and Lowest Temperatures by Day in a Month

```bash
python3 index.py -c 2005/6 /path/to/files
```
<img width="515" alt="image" src="https://github.com/AhsanNazeef/Weatherman-Python/assets/51314116/1a2b94bf-c649-48ad-a240-d7fc993ecb21">

### Contributing
```markdown
## Contributing

Contributions are welcome! If you find any issues or want to add features, feel free to open a pull request or create an issue.
