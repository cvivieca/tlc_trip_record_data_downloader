
# NYC Taxi Data Download Script

This script is designed to download NYC taxi trip data in the parquet format from the NYC Taxi & Limousine Commission website. The data covers yellow taxi trips in New York City from January 2009 to December 2022.

The script uses the `urllib` library to download the data from the web and saves the downloaded files in subdirectories named after the year of the data. It also uses the `tqdm` library to display a progress bar during the download process.

## Requirements

To run this script, you will need:

- Python 3.x (tested with Python 3.10.9)
- `urllib` library (included with Python)
- `tqdm` library (installable via pip)

## Usage

To use this script, simply download or clone the repository and run the `download_nyc_taxi_data.py` script:
```
pip install -r requirements.txt
```
```
python download_nyc_yellow_taxi_data.py
```

The script will download all parquet files for the specified year range and save each year's files in a separate subdirectory while displaying a progress bar for each download.

By default, the script will download data for all years from 2009 to 2022. You can modify the `YEAR`, `MONTH`, `END_YEAR`, and `END_MONTH` variables at the beginning of the script to change the year range of the data you want to download.

Note that the script will create subdirectories for each year of data in the current working directory, so make sure you have enough disk space before running the script.

## Acknowledgements

The data used in this script is made available by the New York City Taxi & Limousine Commission under the [Open Data Policy](https://opendata.cityofnewyork.us/).
