import os
import urllib.request
from tqdm import tqdm

YEAR = 2009
MONTH = 1
END_YEAR = 2022
END_MONTH = 12
BASE_URL = 'https://d37ci6vzurychx.cloudfront.net'

while YEAR <= END_YEAR:
    year_dir = f'{YEAR}'
    os.makedirs(year_dir, exist_ok=True)

    while MONTH <= 12:
        if YEAR == END_YEAR and MONTH > END_MONTH:
            break

        # Convert single-digit month to two-digit format
        if len(str(MONTH)) == 1:
            MONTH = '0' + str(MONTH)
        else:
            MONTH = str(MONTH)

        file_name = f'yellow_tripdata_{YEAR}-{MONTH}.parquet'
        file_url = f'{BASE_URL}/trip-data/{file_name}'
        print(f'Downloading {file_name}...')
        
        # Get the file size
        response = urllib.request.urlopen(file_url)
        file_size = int(response.info().get('Content-Length', -1))

        # Download the file with a progress bar
        with open(os.path.join(year_dir, file_name), 'wb') as file, \
                tqdm(unit='B', unit_scale=True, unit_divisor=1024, total=file_size) as progress:
            block_size = 8192
            while True:
                buffer = response.read(block_size)
                if not buffer:
                    break
                file.write(buffer)
                progress.update(len(buffer))

        # Increment month
        MONTH = int(MONTH) + 1

    # Increment year and reset month
    YEAR += 1
    MONTH = 1

print('All files downloaded.')
